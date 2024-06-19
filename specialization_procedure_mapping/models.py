from django.db import models
from specialization.models import Specialization
from procedure.models import Procedure

# Create your models here.

class SpecializationProcedureMapping(models.Model):
    id = models.AutoField(primary_key=True)
    specialization_id   = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    procedure_id        = models.ForeignKey(Procedure,      on_delete=models.PROTECT)
