from django.contrib import admin
from .models import ConsultationMedicine

class ConsultationMedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'consultation_id', 'medicine_id', 'medicine_dosage', 'medicine_timing', 'medicine_modality', 'medicine_duration', 'medicine_instruction')
    list_filter = ('medicine_timing', 'medicine_modality')
    search_fields = ('consultation_id__id', 'medicine_id__medicine_name')

admin.site.register(ConsultationMedicine, ConsultationMedicineAdmin)
