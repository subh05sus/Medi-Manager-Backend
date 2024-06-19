from rest_framework import serializers
from .models import Specialization

# Define the serializer

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Specialization
        fields  = ('id', 
                'name', 
                )