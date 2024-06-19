from django.db import models
from consultation.models import Consultation
from investigation_master.models import InvestigationMaster


# Create your models here.
class ConsultationInvestigation(models.Model):
    id = models.AutoField(primary_key=True)
    consultation_id  = models.ForeignKey(Consultation , on_delete= models.PROTECT)
    investigation_id =  models.ForeignKey(InvestigationMaster , on_delete= models.PROTECT)
    note             = models.TextField(max_length=250, blank=True,null=True)   