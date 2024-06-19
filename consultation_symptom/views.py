from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import ConsultationSymptom
from consultation.models import Consultation

from .serializers import ConsultationSymptomSerializer , ConsultationSymptomListSerializer  

class ConsultationSymptomView(APIView):
    def get(self, request, *args, **kwargs):
        consultation_id = request.query_params.get('consultation_id')
        if consultation_id is not None:
            consultation_symptoms = ConsultationSymptom.objects.filter(consultation_id=consultation_id)
            serializer = ConsultationSymptomSerializer(consultation_symptoms, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Consultation ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = ConsultationSymptomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Consultation symptoms added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import json
import hashlib
def generate_consultation_fingerprint(symptoms):
    sorted_symptoms = sorted(symptoms, key=lambda x: x['symptom_id'])
    
    concatenated_strings = []
    for symptom in sorted_symptoms:
        concatenated_string = f"{symptom['symptom_id']}-{symptom['severity']}"
        concatenated_strings.append(concatenated_string)
    
    json_concatenated_strings = json.dumps(concatenated_strings).encode()
    consultation_fingerprint = hashlib.sha256(json_concatenated_strings).hexdigest()
    
    return consultation_fingerprint


class ConsultationSymptomListView(viewsets.ModelViewSet):
    queryset = ConsultationSymptom.objects.all()
    serializer_class = ConsultationSymptomListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consultation_id']
    def get_queryset(self):
        queryset = ConsultationSymptom.objects.all()
        appointment_id = self.request.query_params.get('appointment_id')
        if appointment_id:
            try:
                consultation = Consultation.objects.get(appointment_id=appointment_id)
                queryset = queryset.filter(consultation_id=consultation.id)
            except Consultation.DoesNotExist:
                # Handle case where no consultation is found for the provided appointment ID
                queryset = ConsultationSymptom.objects.none()
        return queryset
    def list(self, request, *args, **kwargs):
        # Check if 'fingerprint' parameter is present in query parameters
        if 'fingerprint' in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            consultation_symptoms = list(queryset)
            serializer = self.get_serializer(consultation_symptoms, many=True)

            # Generate consultation fingerprint
            consultation_fingerprint = generate_consultation_fingerprint(serializer.data)
            
            # Return response with consultation fingerprint
            response_data = {
                'symptom_fingerprint': consultation_fingerprint,
            }
            return Response(response_data)
        else:
            # Call superclass method to perform default behavior
            return super().list(request, *args, **kwargs)


   

