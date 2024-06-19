from .models import ActivityMapping
from .serializers import ActivityMappingSerializer
from rest_framework import viewsets # new

# Create your views here.

class ActivityMappingViewSet(viewsets.ModelViewSet): # new
    queryset = ActivityMapping.objects.all()
    serializer_class = ActivityMappingSerializer