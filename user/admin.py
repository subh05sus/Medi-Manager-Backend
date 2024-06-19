from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User
# a.get('date_of_birth')
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'phone_number', 'first_name', 'last_name', 'gender', 'age', 'is_doctor', 'is_receptionist', 'is_staff', 'is_superuser', 'display_profile_pic']
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'aadhar', 'gender', 'age', 'date_of_birth','registration_number', 'qualification', 'profile_pic')}),
        ('Address Info', {'fields': ('address', 'postal_code')}),
        ('Activity Info', {'fields': ('last_login',)}),
        ('Permissions', {'fields': ('is_active', 'is_doctor', 'is_receptionist', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'profile_pic'),
        }),
    )

    def display_profile_pic(self, obj):
        if obj.profile_pic:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.profile_pic.url))
        else:
            return 'No image'

    display_profile_pic.short_description = 'Profile Picture'

admin.site.register(User, CustomUserAdmin)
