from rest_framework import serializers
from .models import ActivityMapping

# Define the serializer

class ActivityMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ActivityMapping
        fields  = ('id', 
                   'entity_id',
                   'component_id',
                   'role_id',
                   'specialization_id',
                   'workflow_id',
                )
    


