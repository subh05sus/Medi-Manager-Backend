from .models import ConsultationMedicine
from .serializers import ConsultationMedicineSerializer , AddConsultationMedicineSerializer
from rest_framework import viewsets , status
from rest_framework.views import APIView
from rest_framework.response import Response
from consultation.models import Consultation
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ConsultationMedicineViewSet(viewsets.ModelViewSet): 
    queryset = ConsultationMedicine.objects.all()
    serializer_class = ConsultationMedicineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation_id']
    def get_queryset(self):
        queryset = ConsultationMedicine.objects.all()
        appointment_id = self.request.query_params.get('appointment_id')
        if appointment_id:
            try:
                consultation = Consultation.objects.get(appointment_id=appointment_id)
                queryset = queryset.filter(consultation_id=consultation.id)
            except Consultation.DoesNotExist:
                # Handle case where no consultation is found for the provided appointment ID
                queryset = ConsultationMedicine.objects.none()
        return queryset

class AddConsultationMedicineView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddConsultationMedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
