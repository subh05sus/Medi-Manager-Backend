from django.db import models

# Create your models here.

class VitalMaster(models.Model):
    id = models.AutoField(primary_key=True)
    vital_name       = models.CharField(max_length=100)
    vital_unit       = models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.vital_name

    