from django.contrib import admin
from .models import MedicineMaster

# Register your models here.

class MedicineMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine_name', 'medicine_dosage')
    search_fields = ('id', 'medicine_name')

admin.site.register(MedicineMaster, MedicineMasterAdmin)




