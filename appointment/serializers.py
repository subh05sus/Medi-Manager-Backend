from rest_framework import serializers
from .models import Appointment
from django_filters import rest_framework as filters

from django.contrib.auth.hashers import make_password 
from user.models import User
from booking_slot.models import BookingSlotConfig , Slot , DayGroup
from rest_framework.response import Response
from datetime import datetime

class UserSerializer(serializers.ModelSerializer):
    """
    Get All Users.
    """
    # full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name' ,'gender','age','is_doctor' , 'address', 'postal_code','email', 'phone_number'  ]
        # 'email', 'phone_number' ,'full_name',

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()
    patient_age = serializers.SerializerMethodField()
    patient_gender = serializers.SerializerMethodField()
    calculated_age = serializers.SerializerMethodField()

    def get_calculated_age(self, obj):
        if obj.patient_id.date_of_birth:
            # Calculate age based on date of birth
            today = datetime.now().date()
            age_delta = today - obj.patient_id.date_of_birth
            years = age_delta.days // 365
            months = (age_delta.days % 365) // 30
            days = (age_delta.days % 365) % 30
            return f"{years}-{months}-{days}"
        elif obj.patient_id.age:
            # If date of birth is not provided but age is, return age directly
            return f"{int(obj.patient_id.age)}-{00}-{00}"
        else:
            # If neither date of birth nor age is provided, return None
            return None

    class Meta:
        model = Appointment
        fields = (
            'id',
            'type',
            'status',
            'appointment_datetime',

            'patient_id',
            'patient_name',
            'patient_age',
            'calculated_age',
            'patient_gender',

            'doctor_id',
            'specialization_id',

            'created_by',
            'updated_by',
            'next_appointment',
            'previous_appointment',

            'created',
            'updated',
            'refer_doctor',
            'follow_up_date'
        )
        read_only_fields = ('created', 'updated',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        if not self.context.get('request') or self.context['request'].query_params.get('id'):
            return ret

        return {
            'id': ret.get('id'),
            'type': ret.get('type'),
            'status': ret.get('status'),
            'patient_id': ret.get('patient_id'),
            'doctor_id': ret.get('doctor_id'),
            'patient_name': ret.get('patient_name'),
            'patient_age': self.get_calculated_age(instance),
            'patient_gender': self.get_patient_gender(instance),
            
        }

    def get_patient_name(self, instance):
        patient = instance.patient_id
        return f"{patient.first_name} {patient.last_name}" if patient else None

    def get_patient_age(self, instance):
        patient = instance.patient_id
        if patient and patient.age:
            # Calculate age based on the difference between the current date and the birthdate
            # age = today.year - patient.date_of_birth.year - ((today.month, today.day) < (patient.date_of_birth.month, patient.date_of_birth.day))
            return patient.age
        return None

    def get_patient_gender(self, instance):
        patient = instance.patient_id
        return patient.gender if patient else None



class AppointmentDetailSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient_id', read_only=True)

    class Meta:
        model   = Appointment
        fields  = (
            'id',
            'type',
            'status',
            'appointment_datetime',

            'patient_id',
            'patient_name',

            'doctor_id',
            'specialization_id',

            'created_by',
            'updated_by',
            'next_appointment',
            'previous_appointment',

            'created',
            'updated',
            'refer_doctor',
            # 'refer_specialization',
            'follow_up_date'
        )
        read_only_fields = ('created', 'updated',)


class AppointmentFilter(filters.FilterSet):
    appointment_datetime = filters.DateFilter(field_name='appointment_datetime', lookup_expr='date')
    created = filters.DateFilter(field_name='created', lookup_expr='date')
    # 2024-01-05
    class Meta:
        model   = Appointment
        fields  = ['status',  'type','created', 'appointment_datetime', 'patient_id' ,'doctor_id']

class UserSpecificAppointmentsSerializer(serializers.Serializer):
    user = UserSerializer()
    appointments = AppointmentSerializer(many=True)


from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import date
from decimal import Decimal

def calculate_age(date_of_birth_str):
        today = date.today()
        date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        print("Date of Birth --> " , type(date_of_birth) , date_of_birth)
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        months = today.month - date_of_birth.month - (today.day < date_of_birth.day)
        if months < 0:
            months += 12
        # Convert everything into a year fraction keeping one decimal point
        age += Decimal(months) / Decimal(12)
        return round(age, 2)

class AppointmentCreationSerializer(serializers.ModelSerializer):
    """
    Serializer to be used by receptionist side to create an 
    appointment given the patient detail .
    """
    patient_detail = serializers.DictField(write_only=True)
    slot_detail = serializers.DictField(write_only=True,required=False)
    
    class Meta:
        model   = Appointment
        fields  = ['appointment_datetime', 'type', 'doctor_id', 'specialization_id', 'patient_detail','slot_detail']
        
    def create(self, validated_data):
        patient_detail_data = validated_data.pop('patient_detail')
        print(patient_detail_data)
        patient, _          = User.objects.get_or_create(phone_number=patient_detail_data['phone_number'])
        default_password    = 'alpine12' # validated_data.pop('password', None)
        patient.password    = make_password(default_password)  # Hash the password
        if patient_detail_data.get('first_name'):
            patient.first_name  = patient_detail_data['first_name']
        if patient_detail_data.get('last_name'):
            patient.last_name   = patient_detail_data['last_name']
        # GENDER
        if patient_detail_data.get('gender'):
            patient.gender   = patient_detail_data['gender']
        #AGE
        if patient_detail_data.get('address'):
            patient.address   = patient_detail_data['address']
        if patient_detail_data.get('age'):
            patient.age   = patient_detail_data['age']
        if patient_detail_data.get('age') is None and patient_detail_data.get('date_of_birth') is not None:
            patient.age   = calculate_age(date_of_birth_str=patient_detail_data['date_of_birth'])
            patient.date_of_birth = patient_detail_data['date_of_birth']
        # ^ Calculating and filling Age out of DOB

        if patient_detail_data.get('email'):
            patient.email   = patient_detail_data['email']
        print("address data",patient.address, "Request data:", patient_detail_data.get('address'))
        patient.save()
        validated_data['patient_id'] = patient

        #Now dealing with SLOT DETAIL
        if validated_data.get('slot_detail'):
            slot_detail_data = validated_data.pop('slot_detail')
    
            session_type    = slot_detail_data.get('session')
            slot_number     = slot_detail_data.get('slot_number')

            current_date = validated_data['appointment_datetime'].date()
            user_daygroups = DayGroup.objects.filter(doctor_id= validated_data['doctor_id'] , is_active=True)
            active_daygroup = user_daygroups.first()
        

            try:
                date        = current_date
                weekday     = date.strftime('%a').lower()
                print('Weekday -- >',weekday)
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

            try:
                booking_slot_config = BookingSlotConfig.objects.get(
                day_group = active_daygroup, 
                day       = weekday)
                print(booking_slot_config)
            except BookingSlotConfig.DoesNotExist:
                return Response({'error': 'No booking slot configuration found for this date and doctor.'}, status=404)

            # Check if the slot is already booked
            if Slot.objects.filter(booking_config_id=booking_slot_config, slot_number=slot_number, session_type=session_type).exists():
                return Response({'error': 'The slot is already booked.'}, status=400)

            new_slot = Slot(
                date=date,
                session_type=session_type,
                slot_number=slot_number,
                booking_config_id=booking_slot_config,
                is_booked=True
            )
            new_slot.save()
            validated_data['booking_slot'] = new_slot

     
        
        appointment = Appointment.objects.create(**validated_data)
        return appointment

