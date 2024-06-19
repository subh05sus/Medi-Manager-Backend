from django.db import models
from user.models import User
from entity.models import Entity


class UserEntityMapping(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    entity_id = models.ForeignKey(Entity, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)


    from_date   = models.DateField(auto_now=True)
    to_date     = models.DateField(blank=True)
    updated     = models.DateField(auto_now_add=True)

