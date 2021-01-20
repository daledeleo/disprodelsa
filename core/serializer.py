from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.exceptions import AuthenticationFailed


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields='__all__'

class UsuarioSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioSistema
        fields=("id","creado_por",'date_created','id_email','tipo_de_usuario','nombre','apellido_paterno','apellido_materno',"username")
        extra_kwargs={
            "password":{"write_only":True},
            "currentPassword":{"write_only":True}
        }
        currentPassword=serializers.CharField(required=False,write_only=True)

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super(UsuarioSistemaSerializer,self).create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("username"):
            instance.username = validated_data.get("username",instance.username)
        if validated_data.get("password"):
            if validated_data.get("currentPassword"):
                if check_password(validated_data.get("currentPassword"),instance.password):
                    instance.password=make_password(validated_data.get("password"))
                else:
                    raise AuthenticationFailed("La contraseña actual no coincide..")
            else:
                instance.password=make_password(validated_data.get("password"))
        instance.save()
        return instance
