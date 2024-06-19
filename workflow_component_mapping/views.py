from .models import WorkflowComponentMapping
from .serializers import WorkflowComponentMappingSerializer
from rest_framework import viewsets # new

# Create your views here.

class WorkflowComponentMappingViewSet(viewsets.ModelViewSet): # new
    queryset = WorkflowComponentMapping.objects.all()
    serializer_class = WorkflowComponentMappingSerializer