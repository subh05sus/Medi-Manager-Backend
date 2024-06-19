from django.contrib import admin
from .models import ReferDoctor

# Register your models here.
class ReferDoctorAdmin(admin.ModelAdmin):
    list_display    = ('id', 'user_id', 'doctor_name','specialization_id','phone_number',)
    list_filter     = ('specialization_id','user_id')
    search_fields   = ('id', 'user_id', 'specialization_id__name')

admin.site.register(ReferDoctor, ReferDoctorAdmin)
