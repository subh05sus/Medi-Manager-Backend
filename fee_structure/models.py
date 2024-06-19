from django.db import models
from user.models import User

from enum import Enum

# Create your models here.
# As Suggested by kaibalya -
# New Consultation fee 
# Followup-Consulattaion Fee
# Exceptional
# Date : March 28 , 2024 in Morning StandUp

class COST_TYPES(Enum):
    DOCTOR_FEE     = "DF"
    SEVICE_CHARGE  = "SC"

class FeeType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 60,blank=True ,null=True,unique=True)

    cost_type  = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(status.value, status.name) for status in COST_TYPES],
                                        default     =   'DF',)

    def __str__(self) -> str:
        return self.name

class UserFeeStructure(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    fee_type = models.ForeignKey(FeeType, on_delete=models.PROTECT, null=True)
    fee_amount = models.DecimalField(max_digits=5,
                                     decimal_places=2,
                                blank=True,null=True)
    




