from .models import InvestigationMaster
from .serializers import InvestigationMasterSerializer
from rest_framework import viewsets # new

# Create your views here.

class InvestigationMasterViewSet(viewsets.ModelViewSet): # new
    queryset = InvestigationMaster.objects.all()
    serializer_class = InvestigationMasterSerializer