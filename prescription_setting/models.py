from django.db import models
from user.models import User
from enum import Enum
from django.core.validators import RegexValidator

class ALIGNMENT_TYPES(Enum):
    LEFT     = "LT" 
    RIGHT    = "RT" 
    MIDDLE   = "MD"


# Create your models here.
class PrescriptionSetting(models.Model):
    id = models.AutoField(primary_key=True)

    doctor_id = models.ForeignKey(User,  on_delete=models.CASCADE, 
                    #   related_name='doctor_id',  
                      blank=True,null=True)
    
    doctor_info_is_visible  =  models.BooleanField()
    doctor_info_alignment   = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(align.value, align.name) for align in ALIGNMENT_TYPES],
                                        default     =   'LT',
                                    )
    
    doctor_name             = models.CharField(max_length=120,blank=True,null=True)
    doctor_qualification    = models.CharField(max_length=280,blank=True,null=True)
    registration_number     = models.CharField(unique = True, 
                                                max_length=18,
                                                null=True,
                                                blank=True)
    
    phone_number= models.CharField(max_length=10, 
                                   validators=[RegexValidator(regex   = '^[0-9]{10}$', 
                                                              message = 'Must be a 10-digit number', 
                                                              code    = 'invalid_number')],
                                                                blank = True,
                                                                unique=True)
    entity_info_is_visible  = models.BooleanField()
    entity_info_alignment   = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(align.value, align.name) for align in ALIGNMENT_TYPES],
                                        default     =   'LT',
                                    )
    entity_name             = models.CharField(max_length=100)
    address                 = models.CharField(max_length=250)
    entity_phone_number1    = models.CharField(max_length=10,null=True)
    entity_phone_number2    = models.CharField(max_length=10,blank = True,null=True)

    entity_timing_is_visible    = models.BooleanField()
    entity_startime             = models.TimeField()
    entity_endtime              = models.TimeField()

    doctor_signature_is_visible = models.BooleanField()
    doctor_signature_alignment       = models.CharField(
                                        max_length  =   2,
                                        choices     =   [(align.value, align.name) for align in ALIGNMENT_TYPES],
                                        default     =   'LT',
                                    )
    signature_line_1 = models.TextField(max_length=100,null=True)
    signature_line_2 = models.TextField(max_length=100,null=True)
    # signature_line_1 = models.ImageField(upload_to='signatures_line1/', blank=True, null=True)
    # signature_line_2 = models.ImageField(upload_to='signatures_line2/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.doctor_id and PrescriptionSetting.objects.filter(doctor_id=self.doctor_id).exists():
            existing_instance = PrescriptionSetting.objects.get(doctor_id=self.doctor_id)
            self.id = existing_instance.id
        super().save(*args, **kwargs)