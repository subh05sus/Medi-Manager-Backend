from rest_framework import serializers
from .models import SpecializationProcedureMapping

# Define the serializer

class  SpecializationProcedureMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = SpecializationProcedureMapping
        fields  = ('id', 
                   'specialization_id',
                   'procedure_id',
                )
    


