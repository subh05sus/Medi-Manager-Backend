from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import User as The_User
from djoser import utils
from rest_framework import serializers
from django.contrib.auth import authenticate
from specialization.models import Specialization
from user_specialization_procedure_mapping.serializers import UserSpecializationProcedureMapping , UserSpecializationProcedureMappingSerializer

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'password', 'is_doctor', 'specialization_name')
        read_only_fields = ('id', 'created', 'updated')

    def create(self, validated_data):
        specialization_name = validated_data.pop('specialization_name', None)
        print(validated_data)
        # Create the user instance without the specialization_name field
        temp_data = {}
        user = User.objects.create_user(**validated_data)
        print("newly Created user.id = ", user.id)
        temp_data['user_id'] = user.id

        
        if specialization_name:
            specialization, _ = Specialization.objects.get_or_create(
                name__iexact=specialization_name,
                defaults={'name': specialization_name.capitalize()}
            )
            # Assuming you have a way to link specialization to user, such as a ForeignKey or a method
            temp_data['specialization_id'] = specialization.id
            serializer = UserSpecializationProcedureMappingSerializer(data=temp_data)

            if serializer.is_valid():
                serializer.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Get All Users.
    """
    # full_name = serializers.SerializerMethodField()
    class Meta:
        model = The_User
        fields = ['id', 'aadhar',  'first_name', 'last_name' ,'gender','age','is_doctor' , 'is_receptionist','aadhar', 'registration_number', "qualification",'address', 'postal_code','email', 'phone_number'  ] #for a doctor user

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
class PatientSerializer(serializers.ModelSerializer):
    """
    Get All Patient Connected to Individual Appointments
    """
    # full_name = serializers.SerializerMethodField()
    class Meta:
        model = The_User
        fields = ['id', 'aadhar',  'first_name', 'last_name' ,'gender','age','is_doctor' , 'is_receptionist','aadhar', 'registration_number', "qualification",'address', 'postal_code','email', 'phone_number'  ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"





class UserSpecializationSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='specialization_id.name', read_only=True)

    class Meta:
        model = UserSpecializationProcedureMapping
        fields = ('specialization_name',)


class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    specializations = UserSpecializationSerializer(source='userspecializationproceduremapping_set', many=True, read_only=True)

    class Meta:
        model = The_User
        fields = ['id', 'full_name', 'first_name', 'last_name', 'profile_pic', 'gender', 'age', 'aadhar', 'registration_number', 'address', 'postal_code', 'qualification', 'is_doctor', 'is_receptionist', 'phone_number', 'specializations']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def validate_profile_pic(self, value):
        if not value:
            return value
        if hasattr(value, 'content_type') and 'image' not in value.content_type:
            raise serializers.ValidationError("The file is not an image.")
        return value




# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     email = serializers.EmailField()
