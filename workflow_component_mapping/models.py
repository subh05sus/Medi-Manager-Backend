from django.db import models
from component.models import Component
from workflow.models import Workflow

# Create your models here.

class WorkflowComponentMapping(models.Model):
    id = models.AutoField(primary_key=True)
    workflow_id        = models.ForeignKey(Workflow,      on_delete=models.PROTECT)
    component_id       = models.ForeignKey(Component,      on_delete=models.PROTECT)
