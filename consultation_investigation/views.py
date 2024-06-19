from .models import ConsultationInvestigation
from consultation.models import Consultation
from .serializers import ConsultationInvestigationSerializer , AddConsultationInvestigationSerializer
from rest_framework import viewsets , status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ConsultationInvestigationViewSet(viewsets.ModelViewSet): 
    queryset = ConsultationInvestigation.objects.all()
    serializer_class = ConsultationInvestigationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation_id']
    def get_queryset(self):
        queryset = ConsultationInvestigation.objects.all()
        appointment_id = self.request.query_params.get('appointment_id')
        if appointment_id:
            try:
                consultation = Consultation.objects.get(appointment_id=appointment_id)
                queryset = queryset.filter(consultation_id=consultation.id)
            except Consultation.DoesNotExist:
                # Handle case where no consultation is found for the provided appointment ID
                queryset = ConsultationInvestigation.objects.none()
        return queryset

class AddConsultationInvestigationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddConsultationInvestigationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)