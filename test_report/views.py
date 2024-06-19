from .models import TestReport
from .serializers import TestReportSerializer
from rest_framework import viewsets 

# Create your views here.

class TestReportViewSet(viewsets.ModelViewSet): 
    queryset = TestReport.objects.all()
    serializer_class = TestReportSerializer