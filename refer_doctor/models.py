from django.db import models
from django.core.validators import RegexValidator

from specialization.models import Specialization
from user.models import User


class ReferDoctor(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    doctor_name = models.CharField(max_length=100)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=10, 
                                   validators=[RegexValidator(regex   = '^[0-9]{10}$', 
                                                              message = 'Must be a 10-digit number', 
                                                              code    = 'invalid_number')],
                                   blank = True,
                                   null=True,
                                   unique=True)

