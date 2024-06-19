from django.db import models
from user.models import User
from specialization.models import Specialization
from procedure.models import Procedure


# Create your models here.
class UserSpecializationProcedureMapping(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    specialization_id   = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    procedure_id        = models.ForeignKey(Procedure,      on_delete=models.PROTECT,
                                            blank=True,
                                            null=True)
    class Meta:
        unique_together = ['user_id', 'specialization_id']
