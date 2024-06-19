from rest_framework import serializers
from django.forms.models import model_to_dict
from .models import Consultation
from django.db import transaction
from appointment.models import Appointment

# Define the serializer

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Consultation
        fields  = ('id',  
                'appointment_id',
               
                'status',
                'doctor_id',
                'updated',

                'updated_by',
                'created_by',
                 'created',

                'fee',
                'fee_paid',
                'next_appointment',

                'finding',
                'diagnosis',

                )
class MinimalConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Consultation
        fields  = ('id',  
                'appointment_id',
               
                'status',
                'doctor_id',

                'fee',
                'fee_paid',
                'next_appointment',

                'finding',
                'diagnosis',

                )

from symptom_master.models import SymptomMaster
from appointment.models import APPOINTMENT_STATUSES , Appointment , APPOINTMENT_TYPES
from consultation_symptom.models import ConsultationSymptom , SEVERITY_TYPES
from consultation_symptom.serializers import ConsultationSymptomSerializer

class ConsultationSymptomSerializer(serializers.ModelSerializer):
    symptom_name = serializers.CharField(write_only=True)

    class Meta:
        model = ConsultationSymptom
        fields = ['symptom_name', 'duration', 'severity']




class MetaConsultationSerializer(serializers.ModelSerializer):
    symptoms = serializers.ListField(write_only=True, child=serializers.DictField(), required=False)
    finding = serializers.CharField(allow_blank=True, required=False)
    created_by = serializers.CharField(allow_blank=True, required=False)
    doctor_id = serializers.IntegerField( required=True)
    diagnosis = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Consultation
        fields = ['appointment_id', 'created_by','doctor_id',
                   'symptoms', 'finding', 'diagnosis']

    def create(self, validated_data):
        symptoms_data = validated_data.pop('symptoms', [])
        with transaction.atomic():
            consultation = Consultation.objects.create(**validated_data)
            for symptom_data in symptoms_data:
                symptom_name = symptom_data['symptom_name'].lower()
                duration = symptom_data.get('duration')
                severity = symptom_data.get('severity')

                # Find or create the SymptomMaster instance
                formatted_symptom_name = symptom_name.capitalize()
                symptom, _ = SymptomMaster.objects.get_or_create(symptom_name__iexact=symptom_name, defaults={'symptom_name': formatted_symptom_name})

                # Create or update the ConsultationSymptom instance
                consultation_symptom, created = ConsultationSymptom.objects.update_or_create(
                    consultation_id=consultation,
                    symptom_id=symptom,
                    defaults={
                        'duration': duration,
                        'severity': severity
                    }
                )

        return consultation

    def to_representation(self, instance):
        """Convert model instance into JSON format for response."""
        representation = super().to_representation(instance)
        representation['consultation_id'] = instance.id  # Include consultation_id in the response

        # Query all related symptoms for this consultation and include them in the response
        # symptoms = ConsultationSymptom.objects.filter(consultation_id=instance.id)
        # symptoms_representation = []
        # for symptom in symptoms:
        #     symptom_detail = {
        #         "symptom_name": symptom.symptom_id.symptom_name,  # Assuming symptom_id is a ForeignKey to SymptomMaster
        #         "duration": symptom.duration,
        #         "severity": symptom.severity
        #     }
        #     symptoms_representation.append(symptom_detail)

        # representation['symptoms'] = symptoms_representation
        return representation




    

