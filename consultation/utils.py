from rest_framework import serializers
from django.forms.models import model_to_dict

from consultation_symptom.models import ConsultationSymptom
from consultation_medicine.models import ConsultationMedicine
from .models import Consultation

class ConsultationSymptomSerializer(serializers.ModelSerializer):
    symptom_name = serializers.CharField(source='symptom_id.symptom_name', read_only=True)

    class Meta:
        model = ConsultationSymptom
        fields = (
            'symptom_name',
            'duration',
            'severity',
        )


class ConsultationMedicineSerializer(serializers.ModelSerializer):
    # Use the MedicineMasterSerializer to represent the medicine details
    # medicine_id = MedicineMasterSerializer(read_only=True)
    medicine_name = serializers.CharField(source='medicine_id.medicine_name', read_only=True)
    class Meta:
        model = ConsultationMedicine
        fields = (
                'id',
                'medicine_name',
                'medicine_id',  
                'medicine_dosage',
                'medicine_timing',
                'medicine_modality',
                'medicine_duration',
                'medicine_instruction',  
                )
        
class GetFindingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Consultation
        fields  = (
                    'id',  
                    'finding',
                    'diagnosis',  )