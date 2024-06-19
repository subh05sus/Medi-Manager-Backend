from .models import VisitorContact
from .serializers import VisitorContactSerializer
from rest_framework import viewsets # new

from rest_framework.permissions import AllowAny
# Create your views here.

class VisitorContactViewSet(viewsets.ModelViewSet): 
    permission_classes = [AllowAny]
    queryset = VisitorContact.objects.all()
    serializer_class = VisitorContactSerializer
