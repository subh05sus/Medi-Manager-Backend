from django.contrib import admin
from .models import SavedPatient

class SavedPatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor_id', 'patient_id']
    filter_horizontal = ('tag',)  

admin.site.register(SavedPatient, SavedPatientAdmin)
