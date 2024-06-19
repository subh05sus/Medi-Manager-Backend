from rest_framework import serializers
from django.db import transaction
from .models import ConsultationInvestigation
from consultation.models import Consultation
from investigation_master.models import InvestigationMaster

# Define the serializer

class ConsultationInvestigationSerializer(serializers.ModelSerializer):
    investigation_name = serializers.CharField(source='investigation_id.name', read_only=True)
    class Meta:
        model   = ConsultationInvestigation
        fields  = ('id', 
                    # 'consultation_id', 
                    'investigation_id',
                    'investigation_name',
                    'note',
                )
    
class InvestigationDetailSerializer(serializers.Serializer):
    investigation_name = serializers.CharField(max_length=80)
    note = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
   
class AddConsultationInvestigationSerializer(serializers.Serializer):
    consultation_id = serializers.IntegerField(write_only=True ,  required = False)
    investigations = InvestigationDetailSerializer(many=True, write_only=True)
    # V2 Development
    appointment_id = serializers.IntegerField(write_only=True, required = False)

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

            investigation_data   = validated_data['investigations']
           
           

            for single_data in investigation_data:
                investigation_name = single_data['investigation_name'].lower()
                note = single_data.get('note' , '')

                formatted_investigation_name = investigation_name.capitalize()
                investigation, _ = InvestigationMaster.objects.get_or_create(name__iexact=investigation_name, defaults={'name': formatted_investigation_name})

                # Create or update the ConsultationSymptom instance
                consultation_symptom, created = ConsultationInvestigation.objects.update_or_create(
                    consultation_id=consultation,
                    investigation_id=investigation,
                    defaults={
                        'note': note,
                
                    }
                )

            # Optionally return the created or updated instances
            return ConsultationInvestigation.objects.filter(consultation_id=consultation)

