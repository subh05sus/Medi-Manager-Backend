from django.db import models


class EntityType(models.Model):
    id = models.AutoField(primary_key=True)
    # Name or Workflow template id ???
    name = models.CharField(max_length=50   )
    # Entity Name : Clinic / Poly-clinic / Hospital etc
    def __str__(self) -> str:
        return self.name
#############################################