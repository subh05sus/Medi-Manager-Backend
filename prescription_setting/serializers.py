# serializers.py

from rest_framework import serializers
from .models import PrescriptionSetting, ALIGNMENT_TYPES

class PrescriptionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionSetting
        fields = (
            'id',
            'doctor_id',
            'doctor_info_is_visible',
            'doctor_info_alignment',
            'doctor_name',
            'doctor_qualification',
            'registration_number',
            'phone_number',

            'entity_info_is_visible',
            'entity_info_alignment',
            'entity_name',
            'address',
            'entity_phone_number1',
            'entity_phone_number2',

            'entity_timing_is_visible',
            'entity_startime',
            'entity_endtime',
            
            'doctor_signature_is_visible',
            'doctor_signature_alignment',
            'signature_line_1',
            'signature_line_2',
        )



class AdvPrescriptionSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionSetting
        exclude = []

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        if not instance.doctor_info_is_visible:
            fields_to_exclude = [
                'doctor_info_alignment',
                'doctor_name',
                'doctor_qualification',
                'registration_number',
                'phone_number',
            ]
            for field in fields_to_exclude:
                data.pop(field, None)

        # Check if entity info is visible
        if not instance.entity_info_is_visible:
            fields_to_exclude = [
                'entity_info_alignment',
                'entity_name',
                'address',
                'entity_phone_number1',
                'entity_phone_number2',
            ]
            for field in fields_to_exclude:
                data.pop(field, None)


        if not instance.entity_timing_is_visible:
            fields_to_exclude = [
                'entity_startime',
                'entity_endtime',
            ]
            for field in fields_to_exclude:
                data.pop(field, None)


        if not instance.doctor_signature_is_visible:
            fields_to_exclude = [
                'doctor_signature_alignment',
                'signature_line_1',
                'signature_line_2',
            ]
            for field in fields_to_exclude:
                data.pop(field, None)

        return data
