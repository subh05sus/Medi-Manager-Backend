from rest_framework import serializers
from .models import Component

# Define the serializer

class  ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Component
        fields  = ('id', 
                   'name',
                 
                )
    


