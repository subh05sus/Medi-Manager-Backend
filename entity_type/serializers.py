from rest_framework import serializers
from .models import EntityType

# Define the serializer

class  EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model   = EntityType
        fields  = ('id', 
                   'name',
                )
    


