from rest_framework import serializers
from .models import UserEntityMapping

# Define the serializer

class UserEntityMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = UserEntityMapping
        fields  = ('id', 
                   'user_id',
                   'entity_id',
                   'is_active',
                   'from_date',
                   'to_date',
                   'updated',
              
                )
    


