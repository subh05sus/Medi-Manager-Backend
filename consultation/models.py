from django.db import models
from user.models import User
from specialization.models import Specialization
from appointment.models import Appointment
from enum import Enum

from django.db.models.signals import post_save
from django.dispatch import receiver
from refer_doctor.models import ReferDoctor

# Create your models here.


class CONSULTATION_STATUSES(Enum):
    CREATED     = "CR"
    # IN_PROGRESS = "IP"
    CANCELLED   = "CN"
    # POSTPONED   = "PP"
    CLOSED      = "CL"

class Consultation(models.Model):

    id = models.AutoField(primary_key=True)
    appointment_id  = models.OneToOneField(Appointment ,  on_delete = models.PROTECT)
    created         = models.DateTimeField(auto_now_add=True)
    status          = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(status.value, status.name) for status in CONSULTATION_STATUSES],
                                        default     =   'CR',)

    doctor_id   = models.IntegerField( blank=True , null = True)
    
    updated     = models.DateTimeField(auto_now=True)
    created_by  = models.CharField(max_length = 50, blank=True)
    updated_by  = models.CharField(max_length = 50, blank=True)

    next_appointment = models.DateTimeField(blank=True ,  null =True)
    # template_id = None
    # this to be added soon 
    fee         = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    fee_paid    = models.BooleanField(default = False)
    finding     = models.TextField(max_length=350,blank=True ,null=True)
    diagnosis   = models.TextField(max_length=350,null=True)
    refer_doctor_id = models.ForeignKey(ReferDoctor, 
                                     on_delete=models.CASCADE, 
                                     blank=True,
                                     null=True)


    # symptom_fingerprint     = models.TextField(max_length=255,null=True)
    # medicine_fingerprint    = models.TextField(max_length=255,null=True)

    class Meta:
        ordering = ['created']
        indexes  = [models.Index(fields=['created'])]
    def __str__(self):
        return f"Consultation for {self.appointment_id} with {self.doctor_id}"
    
@receiver(post_save, sender=Consultation)
def update_appointment_status(sender, instance, **kwargs):
    if instance.status == CONSULTATION_STATUSES.CREATED.value:
        # Set the related Appointment status to 'IN_PROGRESS'
        instance.appointment_id.status = 'IP'
        instance.appointment_id.save()
    elif instance.status == CONSULTATION_STATUSES.CLOSED.value:
        # Set the related Appointment status to 'CLOSED'
        instance.appointment_id.status = 'CL'
        instance.appointment_id.save()
    elif instance.status == CONSULTATION_STATUSES.CANCELLED.value:
        # Set the related Appointment status to 'CANCELLED'
        instance.appointment_id.status = 'CN'
        instance.appointment_id.save()