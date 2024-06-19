from .models import Component
from .serializers import ComponentSerializer
from rest_framework import viewsets # new

# Create your views here.

class ComponentViewSet(viewsets.ModelViewSet): # new
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer