from django.db import models
from consultation.models import Consultation
from symptom_master.models import SymptomMaster
from enum import Enum

# Create your models here.
class SEVERITY_TYPES(Enum):
    MILD     = "MLD"
    MEDIUM    = "MED"
    SEVERE      = "SEV"

class ConsultationSymptom(models.Model):
    id = models.AutoField(primary_key=True)
    consultation_id  = models.ForeignKey(Consultation , on_delete= models.PROTECT)
    symptom_id       = models.ForeignKey(SymptomMaster , on_delete= models.PROTECT)
    duration         = models.TextField(blank=True,null=True) #No of days its occuring
    severity         = models.CharField(
                                        max_length  =   20,
                                        # choices     =   [(types.value, types.name) for types in SEVERITY_TYPES],
                                        # default     =   'MLD', # For Initial Appointment
                                        null=True,
                                        blank=True
                                    )

    class Meta:
        # Ensure uniqueness of symptom for each consultation
        unique_together = ('consultation_id', 'symptom_id')