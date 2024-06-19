from rest_framework import serializers
from .models import SymptomMaster

class SymptomMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomMaster
        fields = ['id','symptom_name']

# class SymptomMasterListSerializer(serializers.Serializer):
#     symptom_names = serializers.ListField(
#         child=serializers.CharField(max_length=80))

#     def create(self, validated_data):
#         symptom_names = validated_data.get('symptom_names', [])
#         # Fetch all symptoms that already exist
#         existing_symptoms = SymptomMaster.objects.filter(symptom_name__in=symptom_names).values_list('symptom_name', flat=True)
#         existing_symptom_set = set(existing_symptoms)
#         new_symptom_names = [name.title() for name in symptom_names if name not in existing_symptom_set]
        
#         new_symptoms = [SymptomMaster(symptom_name=name) for name in new_symptom_names]
        
#         SymptomMaster.objects.bulk_create(new_symptoms)
#         return SymptomMaster.objects.filter(symptom_name__in=new_symptom_names)

