from rest_framework import serializers
from .models import Role

# Define the serializer

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Role
        fields  = ('id', 
                'name', 
                )
    


