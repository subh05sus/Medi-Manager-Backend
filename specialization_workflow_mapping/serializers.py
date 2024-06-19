from rest_framework import serializers
from .models import SpecializationWorkflowMapping

# Define the serializer

class  SpecializationWorkflowMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = SpecializationWorkflowMapping
        fields  = ('id', 
                   'specialization_id',
                   'workflow_id',
                )
    


