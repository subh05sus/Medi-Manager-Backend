from django.db import models


# Create your models here.

class Component(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=50)

# name may be modified into componenet-characteristics ????
    