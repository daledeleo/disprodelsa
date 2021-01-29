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

# Create your views here.
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        try:
            decoded_payload = jwt_decode_handler(request.headers['Token'])
            user = UsuarioSistema.objects.get(id=decoded_payload['user_id'])
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
    queryset= UsuarioSistema.objects.all()
    serializer_class=UsuarioSistemaSerializer

class UserLogin(viewsets.ViewSet):
    permission_classes  = (AllowAny,)

    def create(self,request):
        username= request.data.get("username",'')
        password=request.data.get('password','')
        try:
            user=UsuarioSistema.objects.get(username=username)
        except UsuarioSistema.DoesNotExist:
            user = None
        if user is not None:
            if check_password(password,user.password):  
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                payload['tipo_de_usuario']=user.tipo_de_usuario
                token = jwt_encode_handler(payload)
                return Response({'token':token,
                                 'username':user.username,
                                 "email":str(user.id_email),
                                 "type_user":user.tipo_de_usuario})
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_404_NOT_FOUND)