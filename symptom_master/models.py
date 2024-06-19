from django.db import models

# Create your models here.

class SymptomMaster(models.Model):
    id = models.AutoField(primary_key=True)
    symptom_name       = models.CharField(max_length=80,unique=True)

    def __str__(self):
        return self.symptom_name
    
