from django.contrib import admin
from .models import Role

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Role, RoleAdmin)
