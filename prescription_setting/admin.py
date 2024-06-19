from django.contrib import admin
from .models import PrescriptionSetting

class PrescriptionSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor_id', 'doctor_info_is_visible', 'doctor_info_alignment',
                    'doctor_name', 'doctor_qualification', 'registration_number',
                    'phone_number', 'entity_info_is_visible', 'entity_info_alignment',
                    'entity_name', 'address', 'entity_phone_number1', 'entity_phone_number2',
                    'entity_timing_is_visible', 'entity_startime', 'entity_endtime',
                    'doctor_signature_is_visible', 'signature_line_1', 'signature_line_2']
    
    list_filter = ['doctor_info_is_visible', 'entity_info_is_visible', 'entity_timing_is_visible', 'doctor_signature_is_visible']
    
    search_fields = ['doctor_name', 'doctor_qualification', 'entity_name', 'address']

    fieldsets = (
        ('Doctor Information', {
            'fields': ('doctor_id', 'doctor_info_is_visible', 'doctor_info_alignment',
                       'doctor_name', 'doctor_qualification', 'registration_number',
                       'phone_number',)
        }),
        ('Entity Information', {
            'fields': ('entity_info_is_visible', 'entity_info_alignment',
                       'entity_name', 'address', 'entity_phone_number1', 'entity_phone_number2',)
        }),
        ('Entity Timing', {
            'fields': ('entity_timing_is_visible', 'entity_startime', 'entity_endtime',)
        }),
        ('Doctor Signature', {
            'fields': ('doctor_signature_is_visible', 'signature_line_1', 'signature_line_2',)
        }),
    )

admin.site.register(PrescriptionSetting, PrescriptionSettingAdmin)
