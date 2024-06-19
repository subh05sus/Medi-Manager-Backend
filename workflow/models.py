from django.db import models
# Create your models here.


class Workflow(models.Model):
    id = models.AutoField(primary_key=True)
    # Name or Workflow template id ???
    name = models.CharField(max_length=50 ,blank=True)