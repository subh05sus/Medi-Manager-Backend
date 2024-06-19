from django.db import models

from medicine_master.models import MedicineMaster
from consultation_medicine.models import MEDICINE_TIMING , MEDICINE_TIMING_FOOD_WISE
from investigation_master.models import InvestigationMaster
from user.models import User
from enum import Enum


# Create your models here.

class COLLECTION_TYPES(Enum):
    INVESTIGATION_SET   = "IS"
    MEDICINE_SET        = "MS"
    VITAL_SET      = "VS"

class TemplateMaster(models.Model):
    """
    Actually it should be named as Collections or grouping , 
    but as the name has been decided by mihir bhai; 
    and no one wanted to discuss on the nomenclature part, 
    I am keeping the same.
    """
    id = models.AutoField(primary_key=True)
    template_name  = models.CharField(max_length=50 ,  blank=True)
    template_type  =  models.CharField(
                                        max_length  =   2,
                                        choices     =   [(type.value, type.name) for type in COLLECTION_TYPES],
                                        default     =   'MS',)
    user_id =  models.ForeignKey(User , on_delete= models.PROTECT,null=True)

    def __str__(self) -> str:
        return f"Consultation : {self.template_name} for {self.template_type}"


class MedicineSet(models.Model):
    id = models.AutoField(primary_key=True)
    collection_id   = models.ForeignKey(TemplateMaster, on_delete=models.PROTECT, related_name='medicine_sets')
    medicine_id     = models.ForeignKey(MedicineMaster, on_delete= models.PROTECT)

    medicine_dosage = models.CharField(max_length=20, 
                                        #   decimal_places=1, #!Keeping decimal for half-tablet (case : kids)
                                          blank=True,
                                          null=True) 

    medicine_timing = models.CharField(
                                        max_length  =   100,
                                        # choices     =   [(time.value, time.name) for time in MEDICINE_TIMING],
                                        # default     =   'MN',  # Morning is the default time
                                       blank=True,null=True) 
    medicine_modality = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(time_f.value, time_f.name) for time_f in MEDICINE_TIMING_FOOD_WISE],
                                        default     =   'AF',    blank=True,null=True) 
    medicine_duration       =     models.CharField(max_length=100 , blank=True , null = True)
    medicine_instruction    = models.TextField(max_length=250 , blank=True, null = True)

class InvestigationSet(models.Model):
    id = models.AutoField(primary_key=True)
    collection_id    = models.ForeignKey(TemplateMaster, on_delete=models.PROTECT, related_name='investigation_sets')
    investigation_id =  models.ForeignKey(InvestigationMaster , on_delete= models.PROTECT)
    note             = models.TextField(max_length=250, blank=True,null=True)   
    

