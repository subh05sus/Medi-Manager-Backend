from rest_framework import serializers
from .models import MedicineMaster
from django.db import transaction

from consultation.models import Consultation

# Define the serializer

class MedicineMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MedicineMaster
        fields  = ('id', 
                   'medicine_name',
                   'medicine_dosage',
              
                )
    


class Serializer(serializers.Serializer):
    consultation_id = serializers.IntegerField(write_only=True)
    symptoms = MedicineMasterSerializer(many=True, write_only=True)

    def create(self, validated_data):
        with transaction.atomic():
            consultation_id = validated_data['consultation_id']
            symptoms_data   = validated_data['symptoms']
            consultation    = Consultation.objects.get(id=consultation_id)

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

            # Optionally return the created or updated instances
            return ConsultationSymptom.objects.filter(consultation_id=consultation)