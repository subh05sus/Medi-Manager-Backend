from django.db import models
from user.models import User
from entity.models import Entity
from django.utils import timezone
import json

class DayGroup(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_id   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='day_groups',null=True)
    name        = models.CharField(max_length=100) #ConfigurationName
    is_active   = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.name} for {self.doctor_id}"

    class Meta:
        unique_together = ('doctor_id', 'name')  

class BookingSlotConfig(models.Model):
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES,default='mon')
    # doctor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_slots',null=True)
    
    id = models.AutoField(primary_key=True)
    day_group = models.ForeignKey(DayGroup, on_delete=models.CASCADE, related_name='booking_slots',null=True)

    morning_slots_is_active = models.BooleanField(default=False)
    morning_start_time = models.TimeField(null=True, blank=True)
    morning_end_time = models.TimeField(null=True, blank=True)

    afternoon_slots_is_active = models.BooleanField(default=False)
    afternoon_start_time = models.TimeField(null=True, blank=True)
    afternoon_end_time = models.TimeField(null=True, blank=True)

    evening_slots_is_active = models.BooleanField(default=False)
    evening_start_time = models.TimeField(null=True, blank=True)
    evening_end_time = models.TimeField(null=True, blank=True)

    morning_slots = models.IntegerField(default=0)
    afternoon_slots = models.IntegerField(default=0)
    evening_slots = models.IntegerField(default=0)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"BookingSlot for {self.day} in {self.day_group}'s schedule"
    
    def get_slots_for_session(self, session_type):
        if session_type == 'morning':
            return self.morning_slots if self.morning_slots_is_active else 0
        elif session_type == 'afternoon':
            return self.afternoon_slots if self.afternoon_slots_is_active else 0
        elif session_type == 'evening':
            return self.evening_slots if self.evening_slots_is_active else 0
        else:
            return 0 

    class Meta:
        # Assuming each day group can only have one booking slot setup
        unique_together = ('day_group','day')

class Slot(models.Model):
    SESSION_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    date =  models.DateField(null=True)
    booking_config_id = models.ForeignKey(BookingSlotConfig, on_delete=models.CASCADE, related_name='individual_slots',null=True)
    session_type = models.CharField(max_length=9, choices=SESSION_CHOICES)
    slot_number = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.booking_config_id.day} {self.session_type.capitalize()} Slot {self.slot_number} - {'Booked' if self.is_booked else 'Available'}"

    class Meta:
        unique_together = ('booking_config_id', 'session_type', 'slot_number')