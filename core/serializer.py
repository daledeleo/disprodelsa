from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.exceptions import AuthenticationFailed
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from django.db import models


def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year

    hour=date.hour
    minute=date.minute
    seconds=date.second
    messsage = "{} de {} del {}, {}:{}:{}".format(day, month, year,hour,minute,seconds)
    return messsage

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields='__all__'

    def create(self, validated_data):
        subject="Ahora forma parte de nuestro equipo"
        from_email='leonelmen64@gmail.com'
        to_email=validated_data['email']
        
        with open("templates/email.txt") as f:
            type_user=''
            if(validated_data['type_user']=="1"):
                type_user="Administrador"
            elif(validated_data['type_user']=="2"):
                type_user='Químico Sr'
            elif (validated_data['type_user']=="3"):
                type_user="Químico Jr"
            else:
                type_user="Paciente"
            signup_message=f.read()
            message= EmailMultiAlternatives(subject=subject,
            body=signup_message, from_email=from_email,to=[to_email])
            d4 = current_date_format(datetime.now())
            d={'type_user': type_user,
            "dia_actual":d4}
            html_template=get_template("email.html").render(d)
            message.attach_alternative(html_template,'text/html')
            message.send()
        return super(EmailSerializer,self).create(validated_data)

class UsuarioSistemaSerializer(serializers.ModelSerializer):
    currentPassword=serializers.CharField(required=False,write_only=True)
    class Meta:
        model=User
        fields=("id",'nombre','apellido_paterno','apellido_materno','tipo_usuario','creado_por',
        'date_created','password','currentPassword','username','email','is_staff','is_superuser')
        extra_kwargs = {            
            'password': {'write_only': True},
            'currentPassword': {'write_only': True},
        }

    def create(self,validated_data):   
        validated_data['password']=make_password(validated_data['password'])
        return super(UsuarioSistemaSerializer,self).create(validated_data) 

    def update(self, instance, validated_data):
        if validated_data.get("username"):
            instance.username = validated_data.get("username",instance.username)
            instance.email = validated_data.get("email",instance.email)
            instance.tipo_usuario = validated_data.get("tipo_usuario",instance.tipo_usuario)
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
    

