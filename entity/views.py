from .models import Entity
from .serializers import EntitySerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets # new

# Create your views here.

class EntityViewSet(viewsets.ModelViewSet): # new
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer