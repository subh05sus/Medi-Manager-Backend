from django.db import models

# Create your models here.

class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    # Name or Workflow template id ???
    name = models.CharField(max_length=30,blank=True)
    growth_required = models.BooleanField(default=False)
    vital_required = models.BooleanField(default=False)
