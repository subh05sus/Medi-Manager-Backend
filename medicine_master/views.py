from .models import MedicineMaster
from .serializers import MedicineMasterSerializer
from rest_framework import viewsets # new

# Create your views here.

class MedicineMasterViewSet(viewsets.ModelViewSet): # new
    queryset = MedicineMaster.objects.all()
    serializer_class = MedicineMasterSerializer