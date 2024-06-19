from django.contrib import admin
from .models import PatientVital

class PatientVitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'specialization_id', 'appointment_id', 'vital_id', 'vital_value')
    list_filter = ('specialization_id', 'appointment_id')
    search_fields = ('patient_id__username', 'vital_id__vital_name')
    raw_id_fields = ('patient_id', 'specialization_id', 'appointment_id', 'vital_id')
    ordering = ('id',)

admin.site.register(PatientVital, PatientVitalAdmin)
