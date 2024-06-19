from rest_framework import serializers
from .models import Procedure

# Define the serializer

class  ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Procedure
        fields  = ('id', 
                   'name',
                   'growth_required',
                   'vital_required',
                )
    


