from .models import SpecializationWorkflowMapping
from .serializers import SpecializationWorkflowMappingSerializer
from rest_framework import viewsets # new

# Create your views here.

class SpecializationWorkflowMappingViewSet(viewsets.ModelViewSet): # new
    queryset = SpecializationWorkflowMapping.objects.all()
    serializer_class = SpecializationWorkflowMappingSerializer