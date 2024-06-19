from rest_framework import serializers
from .models import UserRoleMapping

# Define the serializer

class UserRoleMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = UserRoleMapping
        fields  = ('id', 
                   'user_id',
                   'role_id',
              
                )
    


