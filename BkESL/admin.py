from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Consumption, Billed_unit, Eht_consumer_unit,Vigilance_data,Image


@admin.register(Consumption)
class CONSUMPTIONAdmin(ImportExportModelAdmin):
    pass
@admin.register(Billed_unit)
class BILLED_UNIT(ImportExportModelAdmin):
    pass
@admin.register(Eht_consumer_unit)
class EHT_CONSUMER_UNIT(ImportExportModelAdmin):
    pass
@admin.register(Vigilance_data)
class VIGILANCE_DATA(ImportExportModelAdmin):
    pass
@admin.register(Image)
class IMAGE(ImportExportModelAdmin):
    pass


