from django.contrib import admin
from .models import UserEntityMapping

# Register your models here.
class UserEntityMappingAdmin(admin.ModelAdmin):
    list_display    = ('id', 'user_id', 'entity_id','is_active','from_date','to_date','updated')
    list_filter     = ('entity_id',)
    search_fields   = ('id', 'user_id__username', 'entity_id__name')

admin.site.register(UserEntityMapping, UserEntityMappingAdmin)
