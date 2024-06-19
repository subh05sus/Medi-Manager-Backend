from .models import PatientVital
from .serializers import PatientVitalSerializer
from rest_framework import viewsets 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from vital_master.models import VitalMaster

# Create your views here.

class PatientVitalViewSet(viewsets.ModelViewSet): 
    queryset = PatientVital.objects.all()
    serializer_class = PatientVitalSerializer

class SelfPatientVitalView(APIView):
    def get(self, request, *args, **kwargs):
        session_user = request.user
        mappings = PatientVital.objects.filter(user_id=session_user.id)
        serializer = PatientVitalSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        session_user = request.user
        request_data = request.data.copy()
        request_data['user_id'] = session_user.id
        specialization_name = request_data.pop('specialization_name', None)
        if specialization_name:
            specialization, _ = VitalMaster.objects.get_or_create(name__iexact=specialization_name,
                                                                     defaults={'name': specialization_name.capitalize()})
            request_data['specialization_id'] = specialization.id
            print(request_data)

        serializer = PatientVitalSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)