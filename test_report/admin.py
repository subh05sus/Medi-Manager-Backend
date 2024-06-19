from django.contrib import admin
from .models import TestReport

@admin.register(TestReport)
class TestReportAdmin(admin.ModelAdmin):
    list_display = ('document_label', 'appointment_id', 'user_id', 'document_path')
    list_filter = ('appointment_id', 'user_id')
    search_fields = ('document_label', 'appointment_id__id', 'user_id__username')
    readonly_fields = ('document_path',)

    def appointment_id(self, obj):
        return obj.appointment_id_id

    appointment_id.short_description = 'Appointment ID'