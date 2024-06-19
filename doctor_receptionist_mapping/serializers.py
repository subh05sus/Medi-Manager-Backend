from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import DoctorReceptionistMapping


# Define the serializer

class DoctorReceptionistMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DoctorReceptionistMapping
        fields  = ('id', 
                   'doctor_data',
                   'receptionist_data',
                )
    
class DoctorReceptionistMappingFilter(filters.FilterSet):
    class Meta:
        model   = DoctorReceptionistMapping
        fields  = ('id', 
                   'doctor_data',
                   'receptionist_data',)
