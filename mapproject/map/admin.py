from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Data

class DataImportExportAdmin(ImportExportModelAdmin):
    list_display = ('city', 'lat', 'long', 'ttlsignals', 'manuf',)

admin.site.register(Data, DataImportExportAdmin)
# Register your models here.
