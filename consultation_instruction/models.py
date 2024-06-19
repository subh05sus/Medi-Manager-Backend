from django.db import models
from consultation.models import Consultation


# Create your models here.
class ConsultationInstruction(models.Model):
    id = models.AutoField(primary_key=True)
    consultation_id     = models.ForeignKey(Consultation , on_delete= models.PROTECT)
    instruction         = models.TextField(max_length=500, blank  = True)
