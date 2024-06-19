from django.db import models
from specialization.models import Specialization
from workflow.models import Workflow

# Create your models here.

class SpecializationWorkflowMapping(models.Model):
    id = models.AutoField(primary_key=True)
    specialization_id   = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    workflow_id        = models.ForeignKey(Workflow,      on_delete=models.PROTECT)
