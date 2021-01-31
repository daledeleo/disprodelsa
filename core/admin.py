from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from core.models import *
# Register your models here.
@admin.register(Email, User)
class ViewAdmin(ImportExportModelAdmin):
    pass
