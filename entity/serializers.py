from rest_framework import serializers
from .models import Entity

# Define the serializer

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model   = Entity
        fields  = ('id', 
                   'created',
                'name', 
                'type',
                'email',
                'website',
                'phone_number1',
                'phone_number2',
                'address',
                'country',
                'state',
                'postal_code',
                'updated',

                )
    


