from django.contrib import admin
from .models import Entity

class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'email', 'website', 'phone_number1', 'phone_number2', 'address', 'country', 'state', 'postal_code', 'created', 'updated')
    list_filter = ('type', 'country', 'state')
    search_fields = ('id', 'name', 'email', 'address')

admin.site.register(Entity, EntityAdmin)