from django.db import models
from specialization.models import Specialization
from workflow.models import Workflow
from entity.models import Entity
from component.models import Component
from role.models import Role

# Create your models here.
# Specialization Workflow omponent Entity Role
class ActivityMapping(models.Model):
    id = models.AutoField(primary_key=True)
    entity_id           = models.ForeignKey(Entity,         on_delete=models.PROTECT)
    component_id        = models.ForeignKey(Component,      on_delete=models.PROTECT)
    role_id             = models.ForeignKey(Role,           on_delete=models.PROTECT)
    specialization_id   = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    workflow_id         = models.ForeignKey(Workflow,       on_delete=models.PROTECT)
