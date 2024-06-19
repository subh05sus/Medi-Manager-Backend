from django.db import models
from user.models import User
from specialization.models import Specialization
from booking_slot.models import  Slot

from enum import Enum

# Create your models here.

class APPOINTMENT_STATUSES(Enum):
    CREATED     = "CR"
    IN_PROGRESS = "IP"
    CANCELLED   = "CN"
    POSTPONED   = "PP"
    CLOSED      = "CL"
    RESCHEDULED = "RC"
    
class APPOINTMENT_TYPES(Enum):
    INITIAL     = "IA" #First-Registration / First-Visit
    FOLLOWUP    = "FA" # Re-Visit
    CLOSED      = "CA" 
 
class Appointment(models.Model):

    id = models.AutoField(primary_key=True)
    appointment_datetime = models.DateTimeField(blank=True,null = True)
    booking_slot = models.ForeignKey(
        Slot,
        on_delete=models.SET_NULL,
        null=True,
        related_name='appointment_booked'
    )
    # ^ can be filtered only using date --  in this format >> { 2024-01-05 }
    status          = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(status.value, status.name) for status in APPOINTMENT_STATUSES],
                                        default     =   'CR',
                                    )
    type          = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(status.value, status.name) for status in APPOINTMENT_TYPES],
                                        default     =   'IA', # For Initial Appointment
                                    )
    patient_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_id', blank=True,null=True)
    doctor_id = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='doctor_id',  blank=True,null=True)
    specialization_id  = models.ForeignKey(Specialization, on_delete=models.PROTECT,related_name='doctor_specialization',blank=True,null=True)

    created_by      = models.CharField(max_length = 50, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    # ^ can be filtered only using date --  in this format >> { 2024-01-05 }
    updated         = models.DateTimeField(auto_now=True)
    updated_by      = models.CharField(max_length = 50,blank=True)

    previous_appointment    = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_appointments')
    next_appointment        = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_appointments')

    refer_doctor            =  models.CharField(max_length = 100, blank=True,null=True)
    # refer_specialization     =  models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='specialization_followup',blank=True,null=True)

    follow_up_date  = models.DateField(blank=True,null = True)

    class Meta:
        ordering    = ['created']
        indexes     = [models.Index(fields=['created'])]
    def __str__(self):
        return f"Appointment with id {self.id} with {self.doctor_id}"
