from rest_framework import serializers
from .models import InvestigationMaster

# Define the serializer

class InvestigationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = InvestigationMaster
        fields  = ('id', 
                   'name',
                #    'medicine_dosage',
              
                )
    


