from django.shortcuts import render
from .models import SavedPatient
from .serializers import SavedPatientSerializer , SavedPatientFilter , PatientSerializer
from rest_framework import viewsets , status , generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from user.models import User




# Create your views here.

class SavedPatientViewSet(viewsets.ModelViewSet): # new
    queryset = SavedPatient.objects.all()
    serializer_class = SavedPatientSerializer


class SavedPatientForSessionUser(APIView):
    def post(self, request):
        request_data = request.data
        user = self.request.user
        request_data['doctor_id'] = user.id
        print(request_data)
        serializer = SavedPatientSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SavedPatientView(generics.ListAPIView):
    serializer_class = SavedPatientSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class = SavedPatientFilter

    def get_queryset(self):
        user = self.request.user
        return SavedPatient.objects.filter(doctor_id=user.id)

