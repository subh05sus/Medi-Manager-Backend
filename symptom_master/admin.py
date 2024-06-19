from django.contrib import admin
from .models import SymptomMaster

# Register your models here.

class SymptomMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'symptom_name')
    search_fields = ('id', 'symptom_name')

admin.site.register(SymptomMaster, SymptomMasterAdmin)
