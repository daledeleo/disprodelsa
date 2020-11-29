from django.db import models
from gsheets import mixins
from uuid import uuid4
spreadsheet_ID='1SZXVAfOmm4BxY126HSdFzXXJnzGAcHfwZQPXO_QK1CU'


class Producto(mixins.SheetPullableMixin,models.Model):
    spreadsheet_id = spreadsheet_ID
    model_id_field = 'id'
    sheet_id_field=model_id_field
    sheet_name='PRODUCTOS'
    data_range = 'A1:AL'
    max_col="AL"

    id = models.CharField(primary_key=True,max_length=255,default=uuid4)
    SKU = models.CharField(max_length=127,blank=True)
    COD_BARRA=models.CharField(max_length=127,blank=True)
    IMAGEN_DISPONIBLE=models.CharField(max_length=127,blank=True)
    LABORATORIO = models.CharField(max_length=127,blank=True)
    VISITADOR = models.CharField(max_length=127,blank=True)
    PRODUCTO = models.CharField(max_length=127,blank=True)
    REGISTRO_SANITARIO = models.CharField(max_length=127,blank=True)
    TIPO_DE_MEDICAMENTO = models.CharField(max_length=127,blank=True)
    PRINCIPIO_ACTIVO = models.CharField(max_length=127,blank=True)
    ESPECIALIDAD = models.CharField(max_length=127,blank=True)
    GRUPO_O_CLASE = models.CharField(max_length=127,blank=True)
    FAMILIA = models.CharField(max_length=127,blank=True)
    REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO = models.CharField(max_length=127,blank=True)
    PROCEDENCIA_PAIS = models.CharField(max_length=127,blank=True)
    UBICACIÓN = models.CharField(max_length=127,blank=True)
    clasificacion = models.CharField(max_length=127,blank=True)
    PESO = models.CharField(max_length=127,blank=True)
    UNIDAD_PESO = models.CharField(max_length=127,blank=True)
    VOLUMEN = models.CharField(max_length=127,blank=True)
    UNIDADES_VOLUMEN = models.CharField(max_length=127,blank=True)
    PRESENTACION = models.CharField(max_length=127,blank=True)
    UNIDADES_PRESENTACIÓN = models.CharField(max_length=127,blank=True)
    UNIDAD = models.CharField(max_length=127,blank=True)
    UNIDADES_POR_EMPAQUE = models.CharField(max_length=127,blank=True)
    PRECIO_1 = models.CharField(max_length=127,blank=True)
    PRECIO_2 = models.CharField(max_length=127,blank=True)
    PRECIO_3 = models.CharField(max_length=127,blank=True)
    PRECIO_DISPRODELSA = models.CharField(max_length=127,blank=True)
    DESCUENTO = models.CharField(max_length=127,blank=True)
    PRECIO_INCLUYE_IVA = models.CharField(max_length=127,blank=True)
    EXISTENCIA_MINIMA = models.CharField(max_length=127,blank=True)
    EXISTENCIA_MAXIMA = models.CharField(max_length=127,blank=True)
    PRODUCTO_ACTIVO = models.CharField(max_length=127,blank=True)
    BAJO_PEDIDO = models.CharField(max_length=127,blank=True)
    DESCRIPCION = models.CharField(max_length=127,blank=True)
    REACCIONES_ADVERSAS = models.CharField(max_length=127,blank=True)
    SOLUCION = models.CharField(max_length=127,blank=True)

    def __str__(self):
        return self.PRODUCTO


class Medico(mixins.SheetPullableMixin,models.Model):
    spreadsheet_id = spreadsheet_ID
    model_id_field = 'id'
    sheet_id_field=model_id_field
    sheet_name='MEDICOS'
    max_col="AZ"
    data_range = 'A1:AZ'

    id = models.IntegerField(primary_key=True)

    id = models.CharField(primary_key=True,max_length=255,default=uuid4)
    FUENTE = models.CharField(max_length=127,blank=True)
    GENERO = models.CharField(max_length=127,blank=True)
    NOMBRE = models.CharField(max_length=127,blank=True)
    CEDULA = models.CharField(max_length=127,blank=True)
    FECHA_DE_NACIMIENTO = models.CharField(max_length=127,blank=True)
    GUSTOS_Y_PREFERENCIAS = models.CharField(max_length=127,blank=True)
    CATEGORIZACION_MEDICO = models.CharField(max_length=127,blank=True)
    CELULAR= models.CharField(max_length=127,blank=True)
    TELEFONO = models.CharField(max_length=127,blank=True)
    ESPECIALIDAD = models.CharField(max_length=127,blank=True)
    ESPECIALIDA_2 = models.CharField(max_length=127,blank=True)
    ESPECIALIDAD_3 = models.CharField(max_length=127,blank=True)
    CLINICA = models.CharField(max_length=127,blank=True)
    DIRECCION = models.CharField(max_length=127,blank=True)
    CIUDAD = models.CharField(max_length=127,blank=True)
    PROVINCIA = models.CharField(max_length=127,blank=True)
    LATITUD_Y_LONGITUD = models.CharField(max_length=127,blank=True)
    DIAS_ATENCION = models.CharField(max_length=127,blank=True)
    HORA_ATENCION = models.CharField(max_length=127,blank=True)
    E_MAIL = models.CharField(max_length=127,blank=True)
    E_MAIL2 = models.CharField(max_length=127,blank=True)
    REALIZADO_POR_1 = models.CharField(max_length=127,blank=True)
    MEDIO_1 = models.CharField(max_length=127,blank=True)
    FECHA_DE_CONTACTO_1 = models.CharField(max_length=127,blank=True)
    RESULTADOS_CONTACTO_1 = models.CharField(max_length=127,blank=True)
    REALIZADO_POR_2 = models.CharField(max_length=127,blank=True)
    MEDIO_2 = models.CharField(max_length=127,blank=True)
    FECHA_DE_CONTACTO_2 = models.CharField(max_length=127,blank=True)
    RESULTADOS_CONTACTO_2 = models.CharField(max_length=127,blank=True)
    REALIZADO_POR_3 = models.CharField(max_length=127,blank=True)
    MEDIO_3 = models.CharField(max_length=127,blank=True)
    FECHA_DE_CONTACTO_3 = models.CharField(max_length=127,blank=True)
    RESULTADOS_CONTACTO_3 = models.CharField(max_length=127,blank=True)
    REALIZADO_POR_4 = models.CharField(max_length=127,blank=True)
    MEDIO_4 = models.CharField(max_length=127,blank=True)
    FECHA_DE_CONTACTO_4 = models.CharField(max_length=127,blank=True)
    RESULTADOS_CONTACTO_4 = models.CharField(max_length=127,blank=True)
    REALIZADO_POR_5 = models.CharField(max_length=127,blank=True)
    MEDIO_5 = models.CharField(max_length=127,blank=True)
    FECHA_DE_CONTACTO_5 = models.CharField(max_length=127,blank=True)
    RESULTADOS_CONTACTO_5 = models.CharField(max_length=127,blank=True)
    REALIZADO_POR_6 = models.CharField(max_length=127,blank=True)
    MEDIO_6 = models.CharField(max_length=127,blank=True)
    FECHA_DE_CONTACTO_6 = models.CharField(max_length=127,blank=True)
    RESULTADOS_CONTACTO_6 = models.CharField(max_length=127,blank=True)
    SGTE_ACCION_A_REALIZAR_POR = models.CharField(max_length=127,blank=True)
    SGTE_ACCION_MEDIO = models.CharField(max_length=127,blank=True)
    SGTE_ACCION_FECHA = models.CharField(max_length=127,blank=True)
    SGTE_ACCION_MOTIVO = models.CharField(max_length=127,blank=True)
    OBSERVACIONES = models.CharField(max_length=127,blank=True)

    def __str__(self):
        return self.NOMBRE


class Ventas(mixins.SheetPullableMixin,models.Model):
    spreadsheet_id=spreadsheet_ID
    model_id_field = 'id'
    sheet_id_field=model_id_field
    sheet_name='VENTAS'

    id = models.CharField(primary_key=True,max_length=255,default=uuid4)
    COD_MEDICO = models.CharField(max_length=127,blank=True)
    MEDICO = models.CharField(max_length=127,blank=True)
    ESPECIALIDAD = models.CharField(max_length=127,blank=True)
    FECHA = models.CharField(max_length=127,blank=True)
    MES = models.CharField(max_length=127,blank=True)
    AÑO = models.CharField(max_length=127,blank=True)
    SKU = models.CharField(max_length=127,blank=True)
    PRODUCTO = models.CharField(max_length=127,blank=True)
    CANTIDAD = models.CharField(max_length=127,blank=True)
    CAJAS = models.CharField(max_length=127,blank=True)
    UNIDADES = models.CharField(max_length=127,blank=True)
    TOTAL_CAJAS_Y_UNIDADES = models.CharField(max_length=127,blank=True)
    TOTAL_SOLO_CAJAS = models.CharField(max_length=127,blank=True)
    TOTAL_UNIDADES = models.CharField(max_length=127,blank=True)
    TOTAL_DOC = models.CharField(max_length=127,blank=True)
    LABORAT = models.CharField(max_length=127,blank=True)
    COD_CLIENTE = models.CharField(max_length=127,blank=True)
    RUC_CI = models.CharField(max_length=127,blank=True)
    CLIENTE = models.CharField(max_length=127,blank=True)
    FACTURA = models.CharField(max_length=127,blank=True)
    TELEFONO1 = models.CharField(max_length=127,blank=True)
    TELEFONO2 = models.CharField(max_length=127,blank=True)
    CELULAR = models.CharField(max_length=127,blank=True)

    def __str__(self):
        return self.FACTURA

class Site(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256, unique=True)
    script = models.CharField(null=False, blank=False, max_length=256)
    def __unicode__(self):
       return u"{0}".format(self.name)