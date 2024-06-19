from django.contrib import admin
from .models import UserSpecializationProcedureMapping

# Register your models here.



@admin.register(UserSpecializationProcedureMapping)
class UserSpecializationProcedureMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'specialization_id', 'procedure_id')
    list_filter = ('user_id', 'specialization_id', 'procedure_id')
    search_fields = ('user_id__username', 'specialization_id__name', 'procedure_id__name')

