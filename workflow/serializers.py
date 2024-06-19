from rest_framework import serializers
from .models import Workflow

# Define the serializer

class  WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Workflow
        fields  = ('id', 
                   'name',
                )
    


