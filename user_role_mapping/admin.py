from django.contrib import admin
from .models import UserRoleMapping

# Register your models here.
class UserRoleMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'role_id')
    list_filter = ('role_id',)
    search_fields = ('id', 'user_id__username', 'role_id__name')

admin.site.register(UserRoleMapping, UserRoleMappingAdmin)
