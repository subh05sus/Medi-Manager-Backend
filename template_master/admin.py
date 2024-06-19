from django.contrib import admin
from .models import TemplateMaster, MedicineSet, InvestigationSet


class MedicineSetInline(admin.TabularInline):
    model = MedicineSet
    extra = 1  

class InvestigationSetInline(admin.TabularInline):
    model = InvestigationSet
    extra = 1

class TemplateMasterAdmin(admin.ModelAdmin):
    list_display    = ('id', 'template_name', 'template_type', 'user_id')  
    search_fields   = ('template_name', 'template_type') 
    list_filter     = ('template_type', 'user_id')  
    inlines         = [MedicineSetInline, InvestigationSetInline]  


admin.site.register(TemplateMaster, TemplateMasterAdmin)
admin.site.register(MedicineSet)  
admin.site.register(InvestigationSet)  
