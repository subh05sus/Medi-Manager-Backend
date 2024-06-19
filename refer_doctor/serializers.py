from rest_framework import serializers
from .models import ReferDoctor

# Define the serializer

class ReferDoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField() 
    class Meta:
        model   = ReferDoctor
        fields  = ('id', 
                #    'user_id',
                   'doctor_name',
                   'specialization_id',
                    'specialization_name',
                   'phone_number',
                )
    def get_specialization_name(self, obj):
        return obj.specialization_id.name
    


