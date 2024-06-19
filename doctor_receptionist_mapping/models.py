from django.db import models
from user.models import User

class DoctorReceptionistMapping(models.Model):
    id = models.AutoField(primary_key=True)

    doctor_data      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_detail', blank=True,null=True)
    receptionist_data = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptionist_detail',blank=True,null=True)
    class Meta:
        # Ensure uniqueness of symptom for each consultation
        unique_together = ('doctor_data', 'receptionist_data')