from django.db import models
from gsheets import mixins
from uuid import uuid4

'''
class Person(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id = '18F_HLftNtaouHgA3fmfT2M1Va9oO-YWTBw2EDsuz8V4'
    model_id_field = 'guid'

    guid = models.CharField(primary_key=True, max_length=255, default=uuid4)

    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.CharField(max_length=127, null=True,
                             blank=True, default=None)
    phone = models.CharField(max_length=127, null=True,
                             blank=True, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name} // {self.email} ({self.guid})'


class Car(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id = '18F_HLftNtaouHgA3fmfT2M1Va9oO-YWTBw2EDsuz8V4'
    sheet_name = 'Sheet2'

    owner = models.ForeignKey(Person, related_name='cars',
                              on_delete=models.CASCADE, null=True, blank=True, default=None)

    brand = models.CharField(max_length=127)
    color = models.CharField(max_length=127)

    def __str__(self):
        return f'{self.color} {self.brand} // Owned by {self.owner} ({self.id})'
'''
# Create your models here.


class Producto(models.Model):
    SKU = models.CharField(max_length=127)
    COD_BARRA=models.CharField(max_length=127)
    IMAGEN_DISPONIBLE=models.CharField(max_length=127)
    LABORATORIO = models.CharField(max_length=127)
    VISITADOR = models.CharField(max_length=127)
    PRODUCTO = models.CharField(max_length=127)
    REGISTRO_SANITARIO = models.CharField(max_length=127)
    TIPO_DE_MEDICAMENTO = models.CharField(max_length=127)
    PRINCIPIO_ACTIVO = models.CharField(max_length=127)
    ESPECIALIDAD = models.CharField(max_length=127)
    GRUPO_O_CLASE = models.CharField(max_length=127)
    FAMILIA = models.CharField(max_length=127)
    REQUIERE_VENTA_CON_RECETA_PRESCRITA_POR_MEDICO = models.CharField(max_length=127)
    PROCEDENCIA_PAIS = models.CharField(max_length=127)
    UBICACIÓN = models.CharField(max_length=127)
    clasificacion = models.CharField(max_length=127)
    PESO = models.CharField(max_length=127)
    UNIDAD_PESO = models.CharField(max_length=127)
    VOLUMEN = models.CharField(max_length=127)
    UNIDADES_VOLUMEN = models.CharField(max_length=127)
    PRESENTACION = models.CharField(max_length=127)
    UNIDADES_PRESENTACIÓN = models.CharField(max_length=127)
    UNIDAD = models.CharField(max_length=127)
    UNIDADES_POR_EMPAQUE = models.CharField(max_length=127)
    PRECIO_1 = models.CharField(max_length=127)
    PRECIO_2 = models.CharField(max_length=127)
    PRECIO_3 = models.CharField(max_length=127)
    PRECIO_DISPRODELSA = models.CharField(max_length=127)
    DESCUENTO = models.CharField(max_length=127)
    PRECIO_INCLUYE_IVA = models.CharField(max_length=127)
    EXISTENCIA_MINIMA = models.CharField(max_length=127)
    EXISTENCIA_MAXIMA = models.CharField(max_length=127)
    PRODUCTO_ACTIVO = models.CharField(max_length=127)
    BAJO_PEDIDO = models.CharField(max_length=127)
    DESCRIPCION = models.CharField(max_length=127)
    REACCIONES_ADVERSAS = models.CharField(max_length=127)
    SOLUCION = models.CharField(max_length=127)

    def __str__(self):
        return self.PRODUCTO


class Medico(models.Model):
    COD = models.CharField(max_length=127)
    FUENTE = models.CharField(max_length=127)
    GENERO = models.CharField(max_length=127)
    NOMBRE = models.CharField(max_length=127)
    CEDULA = models.CharField(max_length=127)
    FECHA_DE_NACIMIENTO = models.CharField(max_length=127)
    GUSTOS_Y_PREFERENCIAS = models.CharField(max_length=127)
    CATEGORIZACION_MEDICO = models.CharField(max_length=127)
    CELULAR_TELEFONO = models.CharField(max_length=127)
    ESPECIALIDAD = models.CharField(max_length=127)
    ESPECIALIDA_2 = models.CharField(max_length=127)
    ESPECIALIDAD_3 = models.CharField(max_length=127)
    CLINICA = models.CharField(max_length=127)
    DIRECCION = models.CharField(max_length=127)
    CIUDAD = models.CharField(max_length=127)
    PROVINCIA = models.CharField(max_length=127)
    LATITUD_Y_LONGITUD = models.CharField(max_length=127)
    DIAS_ATENCION = models.CharField(max_length=127)
    HORA_ATENCION = models.CharField(max_length=127)
    E_MAIL = models.CharField(max_length=127)
    E_MAIL2 = models.CharField(max_length=127)
    REALIZADO_POR_1 = models.CharField(max_length=127)
    MEDIO_1 = models.CharField(max_length=127)
    FECHA_DE_CONTACTO_1 = models.CharField(max_length=127)
    RESULTADOS_CONTACTO_1 = models.CharField(max_length=127)
    REALIZADO_POR_2 = models.CharField(max_length=127)
    MEDIO_2 = models.CharField(max_length=127)
    FECHA_DE_CONTACTO_2 = models.CharField(max_length=127)
    RESULTADOS_CONTACTO_2 = models.CharField(max_length=127)
    REALIZADO_POR_3 = models.CharField(max_length=127)
    MEDIO_3 = models.CharField(max_length=127)
    FECHA_DE_CONTACTO_3 = models.CharField(max_length=127)
    RESULTADOS_CONTACTO_3 = models.CharField(max_length=127)
    REALIZADO_POR_4 = models.CharField(max_length=127)
    MEDIO_4 = models.CharField(max_length=127)
    FECHA_DE_CONTACTO_4 = models.CharField(max_length=127)
    RESULTADOS_CONTACTO_4 = models.CharField(max_length=127)
    REALIZADO_POR_5 = models.CharField(max_length=127)
    MEDIO_5 = models.CharField(max_length=127)
    FECHA_DE_CONTACTO_5 = models.CharField(max_length=127)
    RESULTADOS_CONTACTO_5 = models.CharField(max_length=127)
    REALIZADO_POR_6 = models.CharField(max_length=127)
    MEDIO_6 = models.CharField(max_length=127)
    FECHA_DE_CONTACTO_6 = models.CharField(max_length=127)
    RESULTADOS_CONTACTO_6 = models.CharField(max_length=127)
    SGTE_ACCION_A_REALIZAR_POR = models.CharField(max_length=127)
    SGTE_ACCION_MEDIO = models.CharField(max_length=127)
    SGTE_ACCION_FECHA = models.CharField(max_length=127)
    SGTE_ACCION_MOTIVO = models.CharField(max_length=127)
    OBSERVACIONES = models.CharField(max_length=127)

    def __str__(self):
        return self.NOMBRE


class Ventas(models.Model):
    COD_MEDICO = models.CharField(max_length=127)
    MEDICO = models.CharField(max_length=127)
    ESPECIALIDAD = models.CharField(max_length=127)
    FECHA = models.CharField(max_length=127)
    MES = models.CharField(max_length=127)
    AÑO = models.CharField(max_length=127)
    SKU = models.CharField(max_length=127)
    PRODUCTO = models.CharField(max_length=127)
    CANTIDAD = models.CharField(max_length=127)
    CAJAS = models.CharField(max_length=127)
    UNIDADES = models.CharField(max_length=127)
    TOTAL_CAJAS_Y_UNIDADES = models.CharField(max_length=127)
    TOTAL_SOLO_CAJAS = models.CharField(max_length=127)
    TOTAL_UNIDADES = models.CharField(max_length=127)
    TOTAL_DOC = models.CharField(max_length=127)
    LABORAT = models.CharField(max_length=127)
    COD_CLIENTE = models.CharField(max_length=127)
    RUC_CI = models.CharField(max_length=127)
    CLIENTE = models.CharField(max_length=127)
    FACTURA = models.CharField(max_length=127)
    TELEFONO1 = models.CharField(max_length=127)
    TELEFONO2 = models.CharField(max_length=127)
    CELULAR = models.CharField(max_length=127)

    def __str__(self):
        return self.FACTURA
