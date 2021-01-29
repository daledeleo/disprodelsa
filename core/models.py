from django.db import models
from safedelete import DELETED_VISIBLE_BY_PK, SOFT_DELETE, SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.exceptions import AuthenticationFailed

class Email(models.Model):
    email=models.EmailField(primary_key=True,unique=True)
    date_created=models.DateTimeField(auto_now_add=True, blank=True)
    tipos_usuario=[(None,"Seleccione un tipo de usuario"),("1","Administrador"),("2","QuimicoSr"),("3","QuimicoJr"),("4","Paciente")]
    type_user=models.CharField(max_length=50,blank=False,choices=tipos_usuario)
    creado_por=models.CharField(max_length=50,blank=False)

    def __str__ (self):
        return str(self.email +" - tipo de usuario:  " +self.get_type_user_display())
    
class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido_paterno=models.CharField(max_length=50,blank=False)
    apellido_materno=models.CharField(max_length=50,blank=False)
    
    class Meta:
        abstract=True

class UsuarioSistema(Persona):
    creado_por=models.CharField(max_length=50,blank=False)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50,blank=False)
    date_created=models.DateTimeField(auto_now_add=True)
    id_email=models.OneToOneField(Email, on_delete=models.CASCADE,null=True)
    tipo_de_usuario=models.CharField(max_length=50,blank=False)


    def __str__(self):
        return self.nombre +" " +self.apellido_paterno

    def create(self,validated_data):
        print(validated_data)
        validated_data['password']=make_password(validated_data['password'])
        return super(UsuarioSistema,self).create(validated_data)

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
