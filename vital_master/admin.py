from django.contrib import admin
from .models import VitalMaster
# Register your models here.


class VitalMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'vital_name', 'vital_unit')  
    search_fields = ('vital_name',)  

admin.site.register(VitalMaster, VitalMasterAdmin)
