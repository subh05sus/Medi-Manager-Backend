from django.contrib import admin
from .models import DoctorReceptionistMapping

# Register your models here.



class DoctorReceptionistMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor_data', 'receptionist_data')
    search_fields = ('id', 'doctor_data')

admin.site.register(DoctorReceptionistMapping, DoctorReceptionistMappingAdmin)


