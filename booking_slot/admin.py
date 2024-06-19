from django.contrib import admin
from django.utils.html import format_html_join
from .models import BookingSlotConfig, DayGroup, Slot


class DayGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor_id', 'name', 'is_active')
    list_filter = ('doctor_id', 'is_active')
    search_fields = ('name', 'doctor_id__username')  # Assuming User has a username field

admin.site.register(DayGroup, DayGroupAdmin)


# class BookingSlotInline(admin.TabularInline):
#     model = BookingSlot
#     extra = 1
#     max_num = 1  # Ensures only one slot configuration per Day Group is created
#     fields = (
#         'morning_slots_is_active', 'morning_start_time', 'morning_end_time', 'morning_slots',
#         'afternoon_slots_is_active', 'afternoon_start_time', 'afternoon_end_time', 'afternoon_slots',
#         'evening_slots_is_active', 'evening_start_time', 'evening_end_time', 'evening_slots',
#         'is_active'
#     )

# @admin.register(DayGroup)
# class DayGroupAdmin(admin.ModelAdmin):
#     inlines = [BookingSlotInline]
#     list_display = ('id','doctor_id','name', 'formatted_days',)

#     def formatted_days(self, obj):
#         # Converts day abbreviations to tags
#         days = obj.days or []
#         return format_html_join(
#             ', ',
#             '<span style="background-color: #2849ca; padding: 3px 8px; border-radius: 15px; margin-right: 5px; font-size: smaller;">{}</span>',
#             ((day,) for day in days)
#         )
#     formatted_days.short_description = "Selected Days"

#     class Media:
#         css = {
#             # 'all': ('css/admin_custom.css',)
#         }



class BookingSlotConfigAdmin(admin.ModelAdmin):
    list_display = ('id','day_group', 'day', 'is_active', 'display_morning', 'display_afternoon', 'display_evening')
    list_filter = ('day_group', 'day', 'is_active')
    search_fields = ('day_group', 'day')
    
    def display_morning(self, obj):
        return f"Active: {obj.morning_slots_is_active}, Slots: {obj.morning_slots}, {obj.morning_start_time} - {obj.morning_end_time}"
    display_morning.short_description = "Morning Slot"
    
    def display_afternoon(self, obj):
        return f"Active: {obj.afternoon_slots_is_active}, Slots: {obj.afternoon_slots}, {obj.afternoon_start_time} - {obj.afternoon_end_time}"
    display_afternoon.short_description = "Afternoon Slot"
    
    def display_evening(self, obj):
        return f"Active: {obj.evening_slots_is_active}, Slots: {obj.evening_slots}, {obj.evening_start_time} - {obj.evening_end_time}"
    display_evening.short_description = "Evening Slot"

    fieldsets = (
        (None, {
            'fields': ('day_group', 'day', 'is_active')
        }),
        ('Morning Slot', {
            'fields': ('morning_slots_is_active', 'morning_start_time', 'morning_end_time', 'morning_slots'),
            'classes': ('collapse',)
        }),
        ('Afternoon Slot', {
            'fields': ('afternoon_slots_is_active', 'afternoon_start_time', 'afternoon_end_time', 'afternoon_slots'),
            'classes': ('collapse',)
        }),
        ('Evening Slot', {
            'fields': ('evening_slots_is_active', 'evening_start_time', 'evening_end_time', 'evening_slots'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(BookingSlotConfig, BookingSlotConfigAdmin)



@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking_config_id', 'session_type', 'slot_number', 'is_booked']
    list_filter = ['session_type', 'is_booked']
    search_fields = ['booking_config_id__day', 'session_type', 'slot_number']




