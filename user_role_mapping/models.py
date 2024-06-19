from django.db import models
from role.models import Role

class UserRoleMapping(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.PROTECT, null=True)
    role_id = models.ForeignKey(Role, on_delete=models.PROTECT)
    # Other fields for the UserEntityMapping model
