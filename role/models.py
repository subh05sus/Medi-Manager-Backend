from django.db import models

# Create your models here.
from enum import Enum



class ROLES(Enum):
    PATIENT         = 'PT'
    ENTITY_ADMIN    = 'EA'
    DOCTOR          = 'DR'
    RECEPTIONIST    = 'RC'
################################################################# 


class Role(models.Model):
    id      = models.AutoField(primary_key=True)
    # name    = models.CharField(default = 'PT',max_length=2, 
    #                             choices =[(role.value, role.name) for role in ROLES])
    name    = models.CharField(max_length = 40)
    def __str__(self):
        return self.name
###################################################################