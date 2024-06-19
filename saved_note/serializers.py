from rest_framework import serializers
from .models import SavedNote
from consultation.models import Consultation
from user.models import User

from django.db import transaction



class SavedNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = SavedNote
        fields  = ('id', 
                   'user_id',
                   'consultation_id',
                   'note_type',
                   'title',
                   'note',
              
                )

class AddNoteSerializer(serializers.Serializer):
    consultation_id = serializers.IntegerField(write_only=True, required=False)
    appointment_id = serializers.IntegerField(write_only=True, required = False)

    user_id     = serializers.IntegerField(write_only=True, required = False)
    note_type   = serializers.CharField(write_only=True, required = False)
    title       = serializers.CharField(write_only=True, required = False)
    note        = serializers.CharField(write_only=True, required = False)
    def create(self, validated_data):
        with transaction.atomic():
            appointment_id  = validated_data.get('appointment_id')
            consultation_id = validated_data.get('consultation_id')
            user_id         = validated_data.get('user_id')
           
            if user_id is None:
                user = self.context['request'].user

            note_type   = validated_data.get('note_type')
            note_title  = validated_data.get('title')
            note_body   = validated_data.get('note')

            if note_title is None:
                note_title = note_body
            
            # Check if a consultation exists for the given appointment
            
            if appointment_id:
                consultation = Consultation.objects.filter(appointment_id=appointment_id).first()

            elif consultation_id is not None:
                print('Consultation ID : ',consultation_id)
                consultation    = Consultation.objects.get(id=consultation_id)
            user = User.objects.get(id=user_id)

            saved_note, _ = SavedNote.objects.update_or_create(
                consultation_id=consultation,
                user_id     =   user,
                note_type   =   note_type ,
                title       =   note_title, 
                note        =   note_body   
            )

            # Optionally return the created or updated instances
            return saved_note



