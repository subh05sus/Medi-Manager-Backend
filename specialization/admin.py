from django.contrib import admin
from .models import Specialization

# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Specialization, SpecializationAdmin)
