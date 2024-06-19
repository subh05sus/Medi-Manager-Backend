from django.db import transaction
from rest_framework import serializers
from .models import ConsultationSymptom, SEVERITY_TYPES
from consultation.models import Consultation
from symptom_master.models import SymptomMaster
from symptom_master.serializers import SymptomMasterSerializer

class SymptomDetailSerializer(serializers.Serializer):
    symptom_name = serializers.CharField(max_length=80)
    duration = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    severity = serializers.CharField(max_length=20, allow_blank=True, allow_null=True)


class ConsultationSymptomSerializer(serializers.Serializer):
    consultation_id = serializers.IntegerField(write_only=True, required=False)
    appointment_id = serializers.IntegerField(write_only=True, required = False)
    symptoms = SymptomDetailSerializer(many=True, write_only=True)

    def create(self, validated_data):
        with transaction.atomic():
            appointment_id = validated_data.get('appointment_id')
            consultation_id = validated_data.get('consultation_id')
            print('Appointment ID : ',appointment_id)
            # Check if a consultation exists for the given appointment
            
            if appointment_id:
                consultation = Consultation.objects.filter(appointment_id=appointment_id).first()

            elif consultation_id is not None:
                print('Consultation ID : ',consultation_id)
                # If no appointment given, get the consultation_id is existing for it >>>
                consultation    = Consultation.objects.get(id=consultation_id)

            symptoms_data = validated_data['symptoms']
            created_symptoms = []
            for symptom_data in symptoms_data:
                symptom_name = symptom_data['symptom_name'].lower()
                duration = symptom_data.get('duration')
                severity = symptom_data.get('severity')

                # Find or create the SymptomMaster instance
                # Ensure that the name is stored in a consistent format, -- first letter capitalized
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
                created_symptoms.append(consultation_symptom)

            # Serialize the created/updated symptoms to include their 'id'
            return_data = []
            for symptom in created_symptoms:
                symptom_data = {
                    'symptom_id': symptom.id,
                    'symptom_name': symptom.symptom_id.symptom_name,
                    'duration': symptom.duration,
                    'severity': symptom.severity
                }
                return_data.append(symptom_data)

            # return return_data

            return ConsultationSymptom.objects.filter(consultation_id=consultation_id)

        
class ConsultationSymptomListSerializer(serializers.ModelSerializer):
    symptom_name = serializers.CharField(source='symptom_id.symptom_name', read_only=True)

    class Meta:
        model = ConsultationSymptom
        fields = (
            'id',
            'symptom_id',
            'symptom_name',
            'duration',
            'severity',
        )