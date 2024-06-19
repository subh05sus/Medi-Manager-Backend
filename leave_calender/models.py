from django.db import models

from user.models import User
from entity.models import Entity

# Create your models here.

class AppliedLeave(models.Model):
    id = models.AutoField(primary_key=True)
    entity_id = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    purpose = models.CharField(max_length = 60,blank=True ,null=True,)
    
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.user_id} - from {self.startDate} to {self.endDate}"

    

   
