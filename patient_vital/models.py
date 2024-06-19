from django.db import models
from appointment.models import Appointment
from user.models import User
from specialization.models import Specialization
from vital_master.models import VitalMaster
# Create your models here.

class PatientVital(models.Model):
    id                  = models.AutoField(primary_key=True)
    patient_id          = models.ForeignKey(User, on_delete=models.PROTECT)
    specialization_id   = models.ForeignKey(Specialization, 
                                            on_delete=models.PROTECT,
                                            blank=True,null=True)
    appointment_id  = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    vital_id        = models.ForeignKey(VitalMaster, on_delete=models.CASCADE)
    vital_value     = models.FloatField(null=True,blank=True) 
    
