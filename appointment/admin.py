from django.contrib import admin
from .models import Appointment, APPOINTMENT_STATUSES

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'appointment_datetime', 
                    'booking_slot',
                    'status', 
                    'type',

                    'doctor_id', 
                    'patient_id', 
                    'specialization_id',

                    'next_appointment',
                    'previous_appointment',

                    'refer_doctor',
                    # 'refer_specialization',
                    'follow_up_date'
                    )
    list_filter     = ('status', 'specialization_id')
    search_fields   = ('id', 'created_by', 'updated_by')

    # Customize the display of the 'status' field using a function

    def display_status(self, obj):
        return dict(APPOINTMENT_STATUSES)[obj.status]
    display_status.short_description = 'Status'

admin.site.register(Appointment, AppointmentAdmin)
