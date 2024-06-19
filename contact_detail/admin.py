from django.contrib import admin
from .models import VisitorContact

# Register your models here.
class VisitorContactAdmin(admin.ModelAdmin):
    list_display    = ('id', 'visitor_name', 'email','phone_number','country',
                   'state',)
    # list_filter     = ('specialization_id','user_id')
 

admin.site.register(VisitorContact, VisitorContactAdmin)
