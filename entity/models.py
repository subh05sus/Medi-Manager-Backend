from django.db import models
from entity_type.models import EntityType

# Create your models here.

class Entity(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=50)
    type        = models.ForeignKey(EntityType , on_delete=models.PROTECT,null=True)
    email       = models.EmailField(blank=True)
    website     = models.URLField(max_length = 100,blank = True)

    phone_number1 = models.CharField(max_length=10)
    phone_number2 = models.CharField(max_length=10,blank = True)

    address     = models.CharField(max_length=250)
    country     = models.CharField(max_length=20)
    state       = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10 , blank = True)
    # I am keeping the max_length in PINCODE 10 - refering to Saudi Arabia
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        indexes  = [models.Index(fields=['-created'])]
        




