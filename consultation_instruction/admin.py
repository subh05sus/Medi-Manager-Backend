from django.contrib import admin
from .models import ConsultationInstruction



@admin.register(ConsultationInstruction)
class ConsultationInstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'consultation_id', 'instruction')  
    search_fields = ('id', 'consultation_id', 'instruction')  
    list_filter = ('consultation_id',)  