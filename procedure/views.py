from .models import Procedure
from .serializers import ProcedureSerializer
from rest_framework import viewsets # new

# Create your views here.

class ProcedureViewSet(viewsets.ModelViewSet): # new
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer