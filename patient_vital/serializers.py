from rest_framework import serializers
from .models import PatientVital

# Define the serializer

class  PatientVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model   = PatientVital
        fields  = ('id', 
                   'patient_id',
                   'specialization_id',
                   'appointment_id',
                   'vital_id',
                   'vital_value',
                )
    


