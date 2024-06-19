from rest_framework import serializers
from .models import ConsultationMedicine , MEDICINE_TIMING , MEDICINE_TIMING_FOOD_WISE
from medicine_master.models import MedicineMaster 
from consultation.models import Consultation
from medicine_master.models import MedicineMaster
from django.db import transaction

from consultation.models import Consultation

class MedicineMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MedicineMaster
        fields  = ('id', 
                   'medicine_name',
                   'medicine_dosage',
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


class MedicineDetailSerializer(serializers.Serializer):
    medicine_name = serializers.CharField(max_length=50)
    dosage = serializers.CharField(required=False, allow_blank=True, allow_null=True,)
    timing = serializers.CharField(required=False, allow_blank=True, allow_null=True,)
    modality = serializers.CharField(required=False, allow_blank=True, allow_null=True,)
    duration = serializers.CharField(max_length=50, allow_blank=True, allow_null=True,required=False)
    instruction = serializers.CharField(max_length=200, allow_blank=True, allow_null=True, required=False)

class AddConsultationMedicineSerializer(serializers.Serializer):
    consultation_id = serializers.IntegerField(write_only=True, required=False)
    appointment_id = serializers.IntegerField(write_only=True, required = False)
    medicines = MedicineDetailSerializer(many=True, write_only=True)

    def create(self, validated_data):
        with transaction.atomic():
            appointment_id = validated_data.get('appointment_id')
            consultation_id = validated_data.get('consultation_id')
            
            # Check if a consultation exists for the given appointment
            
            if appointment_id:
                print('Appointment ID : ',appointment_id)
                consultation = Consultation.objects.filter(appointment_id=appointment_id).first()

            elif consultation_id is not None:
                print('Consultation ID : ',consultation_id)
                # If no appointment given, get the consultation_id is existing for it >>>
                consultation    = Consultation.objects.get(id=consultation_id)

            medicines_data = validated_data['medicines']

            for medicine_data in medicines_data:
                medicine_name = medicine_data['medicine_name'].lower()
                medicine_dosage = medicine_data['dosage']
                medicine_timing = medicine_data['timing']
                medicine_modality = medicine_data['modality']
                medicine_duration = medicine_data.get('duration', '')
                medicine_instruction = medicine_data.get('instruction', '')

                formatted_medicine_name = medicine_name.capitalize()
                medicine, _ = MedicineMaster.objects.get_or_create(medicine_name__iexact=medicine_name, defaults={'medicine_name': formatted_medicine_name})

                # Create or update the ConsultationMedicine instance
                consultation_medicine, created = ConsultationMedicine.objects.update_or_create(
                    consultation_id=consultation,
                    medicine_id=medicine,
                    defaults={
                        'medicine_dosage': medicine_dosage,
                        'medicine_timing': medicine_timing,
                        'medicine_modality': medicine_modality,
                        'medicine_duration': medicine_duration,
                        'medicine_instruction': medicine_instruction,
                    }
                )

            # Optionally return the created or updated instances
            return ConsultationMedicine.objects.filter(consultation_id=consultation)


