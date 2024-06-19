from django.shortcuts import render
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import generics , status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import   AppointmentFilter , AppointmentDetailSerializer , UserSpecificAppointmentsSerializer ,AppointmentCreationSerializer
from datetime import datetime
from doctor_receptionist_mapping.models import DoctorReceptionistMapping
from django.http import JsonResponse , HttpResponse
from django.views import View
from django.db.models import Count, Sum
from django.utils.dateparse import parse_date
from test_report.models import TestReport

from django.http import JsonResponse
from django.conf import settings
import os


# Create your views here.

class AppointmentList(generics.ListCreateAPIView):
    queryset            = Appointment.objects.all()
    serializer_class    = AppointmentDetailSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_class     = AppointmentFilter

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Appointment.objects.all()
    serializer_class    = AppointmentDetailSerializer

class UserAppointmentsView(generics.RetrieveAPIView):
    """
    This will be used to get appointment as per session-user.
    Used in Home screen of Doc.
    """
    serializer_class    = UserSpecificAppointmentsSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_class     = AppointmentFilter

    def get_queryset(self):
        user = self.request.user
        appointment_datetime = self.request.query_params.get('appointment_datetime', None)
        if user.is_doctor:
            # If Doctor has logged in
            current_doctor = user.id
        elif user.is_receptionist:
            # If Receptionist is logged in --> 
            # can see the appointments for corresponding doctor
            receptionist_mapping = DoctorReceptionistMapping.objects.get(receptionist_data=user.id)
            current_doctor = receptionist_mapping.doctor_data
        if appointment_datetime:
                print(appointment_datetime)
                return Appointment.objects.filter(doctor_id= current_doctor, )
        if appointment_datetime is None:
            # If no date is provided, filter against today's date
            today = datetime.now().date()
            return Appointment.objects.filter(doctor_id= current_doctor , appointment_datetime__date=today)
        
    def retrieve(self, request, *args, **kwargs):
        queryset    = self.get_queryset()
        queryset    = self.filter_queryset(queryset)
        user        = request.user
        serializer  = self.get_serializer({'user': user, 'appointments': queryset})
        return Response(serializer.data)


def patient_latest_appointments_view(request):
    """
    This view is used to get the latest appointment conducted between a patient and a doctor.
    Used in the home screen of the doctor to get the document for a patient.
    """
    if request.method == 'GET':
  
        appointment_id = request.GET.get('appointment_id')

        if not appointment_id:
            return HttpResponse('Appointment ID is required.', status=400)
        appointment = Appointment.objects.get(pk=appointment_id)
        doctor = appointment.doctor_id
        patient= appointment.patient_id


        recent_appointments = Appointment.objects.filter(doctor_id=doctor.id, patient_id=patient.id, status="CL")
        latest_appointment = recent_appointments.order_by('-created').first()
        

        if latest_appointment:
            # print('Appointment-ID :',latest_appointment.id)
            try:
                test_report = TestReport.objects.get(appointment_id=latest_appointment, document_label="prescription")
                print('Test Report:', test_report)
                
                # Assuming 'document_path' is the field storing the path relative to MEDIA_ROOT
                pdf_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, test_report.document_path.name))
                return JsonResponse({'pdf_url': pdf_url})

            except TestReport.DoesNotExist:
                return JsonResponse({'message': 'No test report found for the latest appointments.'}, status=404)
        else:
            return JsonResponse({'message': 'No past appointment found for this patient.'}, status=404)


    

class AppointmentSummaryView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get a summary of appointments including counts and total fees per date for the logged-in doctor.
        """
        user = request.user  
        if not user.is_doctor:  
            return Response({'error': 'Unauthorized: User is not a doctor'}, status=403)

        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')

        # Parse dates if provided
        start_date = parse_date(start_date_str) if start_date_str else None
        end_date = parse_date(end_date_str) if end_date_str else None

        # Build the filter kwargs dynamically
        filter_kwargs = {'doctor_id': user.id}

        if start_date:
            filter_kwargs['appointment_datetime__date__gte'] = start_date
        if end_date:
            filter_kwargs['appointment_datetime__date__lte'] = end_date
        print('Doctor Id -- >',filter_kwargs['doctor_id'])
        appointments = Appointment.objects.filter(**filter_kwargs).values('appointment_datetime__date').annotate(
            appointment_count=Count('id'),
            consultation_count=Count('consultation', distinct=True),
            total_fees=Sum('consultation__fee')  
        )

        # Serialize and return data
        data = [{
            'date': item['appointment_datetime__date'],
            'appointment_count': item['appointment_count'],
            'consultation_count': item['consultation_count'],
            'total_revenue': item['total_fees']
        } for item in appointments]

        return Response(data)

    
class AppointmentCreateView(APIView):
    def post(self, request):
        request_data = request.data
        user    = request.user
        # Set the time of appointment to current time | 
        request_data['appointment_datetime'] += "T" + str(timezone.now().time())
        print("Data sent from receptionist",request_data )
        if request_data.get('doctor_id') is None:
            if user.is_doctor:
                request_data['doctor_id'] = user.id
            elif user.is_receptionist:
                receptionist_mapping = DoctorReceptionistMapping.objects.get(receptionist_data=user.id)
                mapped_doctor = receptionist_mapping.doctor_data
                request_data['doctor_id'] = mapped_doctor.id
        serializer = AppointmentCreationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AppointmentCreateForPatient(APIView):
    def post(self, request):
        request_data = request.data
        user    = request.user
        # Set the time of appointment to current time | 
        if request_data.get('appointment_datetime') is None:
            request_data['appointment_datetime'] += "T" + str(timezone.now().time())
        
        if request_data.get('patient_id') is None:
            request_data['patient_id'] = user.id
        k = request_data['slot_detail']
        k['date'] = request_data.get('appointment_datetime')
        print("Data sent from receptionist",request_data )
        serializer = AppointmentCreationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)