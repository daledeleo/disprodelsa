from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.permissions import BasePermission, IsAdminUser, AllowAny
from rest_condition import Or
from rest_framework_jwt.utils import jwt_decode_handler ##para poder generar tokens
from django.contrib.auth.hashers import check_password
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


# Create your views here.
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        try:
            decoded_payload = jwt_decode_handler(request.headers['Token'])
            user = User.objects.get(id=decoded_payload['user_id'])
            if user is not None:
                return True
            return False
        except:
            return False

class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, IsAdminUser),)
    queryset= Email.objects.all()
    serializer_class=EmailSerializer

class UsuarioSistemaViewSet(viewsets.ModelViewSet):
    permission_classes = (Or(IsAuthenticated, IsAdminUser),)
    queryset= User.objects.all()
    serializer_class=UsuarioSistemaSerializer
    
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
        d4 = current_date_format(datetime.today())
        print('aqui '+str(instance))
        context={
            'current_user':reset_password_token.user,
            "username":reset_password_token.user.username,
            'email':reset_password_token.user.email,
            'reset_password_url':str(settings.URL_NGROK)+"/"+"Reestablecer-password/reset?token={}".format(
                reset_password_token.key,
            ),
            "dia_actual":d4
        }
        #print(context)
        subject="Reestablecimiento de contraseña"
        from_email= settings.EMAIL_HOST_USER
        to_email=context.get('email')
        with open("templates/email.txt") as f:
            signup_message=f.read()
            message= EmailMultiAlternatives(subject=subject,
            body=signup_message, from_email=from_email,to=[to_email])
          
            html_template=get_template("password_reset.html").render(context)
            message.attach_alternative(html_template,'text/html')
            message.send()


class UserLogin(viewsets.ViewSet):
    permission_classes  = (AllowAny,)
    def create(self,request):
        username= request.data.get("username",'')
        password=request.data.get('password','')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is not None:
            if check_password(password,user.password):  
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                payload['tipo_usuario']=user.tipo_usuario
                token = jwt_encode_handler(payload)
                return Response({'token':token,
                                 'username':user.username,
                                 "email":str(user.email),
                                 "type_user":user.tipo_usuario})
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_404_NOT_FOUND)