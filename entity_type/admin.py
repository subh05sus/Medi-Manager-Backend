from django.contrib import admin
from .models import EntityType

# Register your models here.


class EntityTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(EntityType, EntityTypeAdmin)