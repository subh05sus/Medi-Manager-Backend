from django.db import models
from user.models import User
from taggit.managers import TaggableManager

# Create your models here.
class SavedPatient(models.Model):

    id = models.AutoField(primary_key=True)
    doctor_id   = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='doctor',  blank=True,null=True)
    patient_id  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient', blank=True,null=True)
    tag         = TaggableManager(blank=True,)

    class Meta:
        unique_together = ['doctor_id', 'patient_id']


    


