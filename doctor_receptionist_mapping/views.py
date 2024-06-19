from django.shortcuts import render
from .models import DoctorReceptionistMapping
from .serializers import DoctorReceptionistMappingSerializer , DoctorReceptionistMappingFilter
from rest_framework import viewsets , status , generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from user.models import User

from django.contrib.auth.hashers import make_password 


# Create your views here.

class DoctorReceptionistMappingViewSet(viewsets.ModelViewSet): # new
    queryset = DoctorReceptionistMapping.objects.all()
    serializer_class = DoctorReceptionistMappingSerializer


class MappingReceptionistForSessionUser(APIView):
    def post(self, request):
        user = self.request.user

        request_data = request.data
        receptionist_data = request_data.get('receptionist_detail', None)

        if receptionist_data is None:
            return Response({'error': 'Receptionist Detail is required'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            receptionist, created = User.objects.get_or_create(**receptionist_data)
            receptionist.is_receptionist = True
            receptionist.password = make_password('alpine12')  # Hash the password
            receptionist.save()

        
        data = {'doctor_data': user.id, 'receptionist_data': receptionist.id}
        serializer = DoctorReceptionistMappingSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserReceptionistView(generics.RetrieveAPIView):
    serializer_class = DoctorReceptionistMappingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DoctorReceptionistMappingFilter

    def get_queryset(self):
        user = self.request.user
        print(user.id)
     
        return DoctorReceptionistMapping.objects.filter(doctor_data=user.id, )
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if len(queryset) !=0:
            serializer = self.get_serializer(queryset[0])
            return Response(serializer.data)
     
        return Response({})


