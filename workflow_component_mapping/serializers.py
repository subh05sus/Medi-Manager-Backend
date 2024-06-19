from rest_framework import serializers
from .models import WorkflowComponentMapping

# Define the serializer

class  WorkflowComponentMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = WorkflowComponentMapping
        fields  = ('id', 
                   'component_id',
                   'workflow_id',
                )
    


