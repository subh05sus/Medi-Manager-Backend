from django.contrib import admin
from .models import AppliedLeave 



# @admin.register(Consultation)
class AppliedLeaveAdmin(admin.ModelAdmin):
    list_display = ('id',  'user_id',  'purpose',  'startDate', 'endDate' )  
    search_fields = ('id',  'user_id',  'purpose',  'startDate', 'endDate')  
    list_filter = ( 'user_id', 'startDate', 'endDate' )  

admin.site.register(AppliedLeave, AppliedLeaveAdmin)