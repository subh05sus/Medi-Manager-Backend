from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import SavedPatient
from taggit.models import Tag
from user.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


# Define the serializer

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'age', 'gender'] 



class SavedPatientSerializer(serializers.ModelSerializer):
    patient = UserSerializer(source='patient_id', read_only=True)
    tag = TagSerializer(many=True, required=False) 

    class Meta:
        model = SavedPatient
        fields = ('id','doctor_id', 'patient', 'tag')

class PatientSerializer(serializers.ModelSerializer):
    patient = UserSerializer(source='patient', read_only=True)
    tag = TagSerializer(many=True, required=False) 

    class Meta:
        model = SavedPatient
        fields = ('id','doctor_id', 'patient_id', 'tag')

    
class SavedPatientFilter(filters.FilterSet):
    class Meta:
        model   = SavedPatient
        fields  = ('id', 
                   'doctor_id',
                #    'patient_id',
                #    'tag',
                )
