from .models import EntityType
from .serializers import EntityTypeSerializer
from rest_framework import viewsets # new

# Create your views here.

class EntityTypeViewSet(viewsets.ModelViewSet): # new
    queryset = EntityType.objects.all()
    serializer_class = EntityTypeSerializer