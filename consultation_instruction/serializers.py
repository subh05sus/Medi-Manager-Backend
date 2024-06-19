from rest_framework import serializers
from .models import ConsultationInstruction
from django.db import transaction
from consultation.models import Consultation

# Define the serializer

class ConsultationInstructionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultationInstruction
        fields = ('id',
                   'consultation_id', 
                   'instruction', 
               
                )


class AddConsultationInstructionSerializer(serializers.Serializer):
    instruction = serializers.CharField(max_length=300, allow_blank=True, allow_null=True, required=False)
    appointment_id = serializers.IntegerField(write_only=True, required = False)
    consultation_id = serializers.IntegerField(write_only=True, required=False)
 

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

            instruction_text = validated_data['instruction']

            # Create or update the ConsultationMedicine instance
            consultation_instruction , created = ConsultationInstruction.objects.update_or_create(
                consultation_id=consultation,
                instruction = instruction_text
            )

            # Optionally return the created or updated instances
            return consultation_instruction