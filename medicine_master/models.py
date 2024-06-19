from django.db import models
from enum import Enum

# Create your models here.

class MODALITY_TYPES(Enum):
    AFTER_FOOD     = "AF"
    BEFORE_FOOD    = "BF"
    WITH_FOOD      = "WF"
    EMPTY_STOMACH      = "EA"

class MedicineMaster(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_name       = models.CharField(max_length=50)
    medicine_dosage     = models.CharField(max_length=50,blank=True,null=True)
    # medicine_timing     = models.CharField(max_length=50,blank=True,null=True)

    # medicine_modality          = models.CharField(
    #                                     max_length  =   2,
    #                                     choices     =   [(status.value, status.name) for status in MODALITY_TYPES],
    #                                     default     =   'AF',
    #                                 )
    medicine_form = models.CharField(max_length=50, blank=True , null = True)

    def __str__(self):
        return self.medicine_name