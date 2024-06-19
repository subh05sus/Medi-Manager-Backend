from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ConsultationInvestigation

from consultation_investigation.models import ConsultationInvestigation

@admin.register(ConsultationInvestigation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'consultation_id', 'investigation_id', 'note')  
    search_fields = ('id', 'consultation_id', 'investigation_id')  
    list_filter = ('consultation_id',)  