from django.contrib import admin
from apps.core.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Producto, Medico, Ventas)
class ViewAdmin(ImportExportModelAdmin):
    pass