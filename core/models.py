from django.db import models
from safedelete import DELETED_VISIBLE_BY_PK, SOFT_DELETE, SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager


#Managers
class EmailManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

class UsuarioSistemaManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

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
    #email=models.EmailField()
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50,blank=False)
    date_created=models.DateTimeField(auto_now_add=True, blank=True)
    id_email=models.OneToOneField(Email, on_delete=models.CASCADE, blank=False)
    tipo_de_usuario=models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.nombre +" " +self.apellido_paterno
