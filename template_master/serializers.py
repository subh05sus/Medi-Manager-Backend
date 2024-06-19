from rest_framework import serializers
from .models import TemplateMaster, MedicineSet, InvestigationSet

# Define the serializer

# serializers.py
class GeneralTemplateMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model   = TemplateMaster
        fields  = ( 'id', 
                    'user_id',
                    'template_name',
                    'template_type',
                )


class MedicineSetSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine_id.medicine_name', read_only=True)
    class Meta:
        model = MedicineSet
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


class InvestigationSetSerializer(serializers.ModelSerializer):
    investigation_name = serializers.CharField(source='investigation_id.name', read_only=True)
    class Meta:
        model = InvestigationSet
        fields =  (
            'id',
            'investigation_id',  
            'investigation_name',
            'note',
            
        )

class TemplateMasterSerializer(serializers.ModelSerializer):
    medicine_sets = MedicineSetSerializer(many=True, required=False)
    investigation_sets = InvestigationSetSerializer(many=True, required=False)


    class Meta:
        model = TemplateMaster
        fields = ['id', 'template_name', 'template_type', 'user_id', 'medicine_sets', 'investigation_sets']

    def create(self, validated_data):
        medicine_sets_data = validated_data.pop('medicine_sets', None)
        investigation_sets_data = validated_data.pop('investigation_sets', None)
        template_master = TemplateMaster.objects.create(**validated_data)
        
        if template_master.template_type == 'MS' and medicine_sets_data:
            print("-----")
            for medicine_data in medicine_sets_data:
                MedicineSet.objects.create(collection_id=template_master, **medicine_data)
                
        elif template_master.template_type == 'IS' and investigation_sets_data:
            for investigation_data in investigation_sets_data:
                InvestigationSet.objects.create(collection_id=template_master, **investigation_data)
                
        return template_master



class TemplateMasterWithMedicineSerializer(serializers.ModelSerializer):
    medicine_sets = MedicineSetSerializer(many=True, read_only=True)

    class Meta:
        model = TemplateMaster
        fields = '__all__'  # Include all fields plus the medicine_sets

class TemplateMasterWithInvestigationSerializer(serializers.ModelSerializer):
    investigation_sets = InvestigationSetSerializer(many=True, read_only=True)

    class Meta:
        model = TemplateMaster
        fields = '__all__'  # Include all fields plus the investigation_sets
