from django.db import models
from enum import Enum

from user.models import User
from consultation.models import Consultation

# Create your models here.

class CONSULTATION_STATUSES(Enum):
    FINDING     = "FND"
    DIAGNOSIS  = "DGN"

class SavedNote(models.Model):
    id = models.AutoField(primary_key=True)
    user_id  = models.ForeignKey(User ,  on_delete = models.PROTECT)
    consultation_id  = models.ForeignKey(Consultation ,  on_delete = models.PROTECT)
    note_type          = models.CharField(
                                        max_length  =   3,
                                        choices     =   [(type.value, type.name) for type in CONSULTATION_STATUSES],
                                        default     =   'FND',)
    title =  models.TextField(max_length=255,null=True)
    note   = models.TextField(max_length=350,blank=True ,null=True)

    def __str__(self):
        return f" {self.note_type} note by {self.user_id} for {self.consultation_id}"