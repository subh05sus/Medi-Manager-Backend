from .models import SpecializationProcedureMapping
from .serializers import SpecializationProcedureMappingSerializer
from rest_framework import viewsets # new

# Create your views here.
class SpecializationProcedureMappingViewSet(viewsets.ModelViewSet): # new
    queryset            = SpecializationProcedureMapping.objects.all()
    serializer_class    = SpecializationProcedureMappingSerializer

