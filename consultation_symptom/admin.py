from django.contrib import admin
from .models import ConsultationSymptom

# Register your models here.

class ConsultationSymptomAdmin(admin.ModelAdmin):
    list_display = ('id','consultation_id', 'symptom_id')
    search_fields = ('id', 'symptom_name')

admin.site.register(ConsultationSymptom, ConsultationSymptomAdmin)
