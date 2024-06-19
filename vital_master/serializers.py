from rest_framework import serializers
from .models import VitalMaster

# Define the serializer

class  VitalMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = VitalMaster
        fields  = ('id', 
                   'vital_name',
                   'vital_unit',
                )
    


