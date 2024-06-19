from rest_framework import serializers
from .models import UserSpecializationProcedureMapping
from specialization.models import Specialization
from procedure.models import Procedure
from user.models import User


# Define the serializer

class  UserSpecializationProcedureMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = UserSpecializationProcedureMapping
        fields  = ('id', 
                   'procedure_id',
                   'specialization_id',
                   'user_id', 
                   )
    


class GetUserSpecializationProcedureMappingSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField()  

    class Meta:
        model = UserSpecializationProcedureMapping
        fields = ('id', 'user_id', 'specialization_id',  'specialization_name','procedure_id')  

    def get_specialization_name(self, obj):
        return obj.specialization_id.name

