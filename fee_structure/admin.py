from django.contrib import admin

# Register your models here.
from .models import UserFeeStructure , FeeType

class FeeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','cost_type')  # Customize as needed
    search_fields = ('name',)

# Register the admin class with the associated model
admin.site.register(FeeType, FeeTypeAdmin)

# @admin.register(Consultation)
class UserFeeStructureAdmin(admin.ModelAdmin):
    list_display = ('id',  'user_id',  'fee_type',  'fee_amount', )  
    search_fields = ('id',  'user_id',  'fee_type',  'fee_amount',)  
    list_filter = ( 'user_id',  'fee_type', )  

admin.site.register(UserFeeStructure, UserFeeStructureAdmin)