from django.shortcuts import render
from rest_framework import generics
from .models import Specialization
from .serializers import SpecializationSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class SpecializationList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset            = Specialization.objects.all()
    serializer_class    = SpecializationSerializer
class SpecializationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset        = Specialization.objects.all()
    serializer_class = SpecializationSerializer