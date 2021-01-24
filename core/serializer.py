from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.exceptions import AuthenticationFailed
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import render
from django.conf import settings

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields='__all__'

    def create(self, validated_data):
        subject="ahora forma parte de nuestro equipo"
        from_email='leonelmen64@gmail.com'
        to_email=validated_data['email']
        with open("templates/email.txt") as f:
            signup_message=f.read()
            message= EmailMultiAlternatives(subject=subject,
            body=signup_message, from_email=from_email,to=[to_email])
            html_template=get_template("email.html").render()
            message.attach_alternative(html_template,'text/html')
            message.send()
            #print("llego")
        return super(EmailSerializer,self).create(validated_data)

class UsuarioSistemaSerializer(serializers.ModelSerializer):
    currentPassword=serializers.CharField(required=False,write_only=True)
    class Meta:
        model=UsuarioSistema
        fields=("id","creado_por",'date_created','id_email','tipo_de_usuario','nombre','apellido_paterno',
        'apellido_materno',"username","password","currentPassword")
        extra_kwargs = {            
            'password': {'write_only': True},
            'currentPassword': {'write_only': True}
        }

    def create(self,validated_data):
        print(validated_data)
        validated_data['password']=make_password(validated_data['password'])
        return super(UsuarioSistemaSerializer,self).create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("username"):
            instance.username = validated_data.get("username",instance.username)
            instance.id_email = validated_data.get("id_email",instance.id_email)
            instance.tipo_de_usuario = validated_data.get("tipo_de_usuario",instance.tipo_de_usuario)
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
