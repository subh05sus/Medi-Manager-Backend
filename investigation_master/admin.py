from django.contrib import admin
from .models import InvestigationMaster

# Register your models here.


class InvestigationMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(InvestigationMaster, InvestigationMasterAdmin)


