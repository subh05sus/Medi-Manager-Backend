from django.contrib import admin
from .models import Consultation

# @admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment_id', 'status', 'created','fee','fee_paid','doctor_id','next_appointment')  
    search_fields = ('id', 'status', 'created_by')  
    list_filter = ('status',)  

admin.site.register(Consultation, ConsultationAdmin)
