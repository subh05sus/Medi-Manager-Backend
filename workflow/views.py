from .models import Workflow
from .serializers import WorkflowSerializer
from rest_framework import viewsets # new

# Create your views here.

class WorkflowViewSet(viewsets.ModelViewSet): # new
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer