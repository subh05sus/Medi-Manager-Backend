from .models import VitalMaster
from .serializers import VitalMasterSerializer
from rest_framework import viewsets 

# Create your views here.

class VitalMasterViewSet(viewsets.ModelViewSet): 
    queryset = VitalMaster.objects.all()
    serializer_class = VitalMasterSerializer