from .models import SavedNote
from .serializers import SavedNoteSerializer ,  AddNoteSerializer
from rest_framework import viewsets , status
from rest_framework.views import APIView
from rest_framework.response import Response
from consultation.models import Consultation
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class SavedNoteViewSet(viewsets.ModelViewSet): 
    queryset            = SavedNote.objects.all()
    serializer_class    = SavedNoteSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_fields    = ['consultation_id']
    def get_queryset(self):
        queryset        = SavedNote.objects.all()
        appointment_id  = self.request.query_params.get('appointment_id')
        user_id  = self.request.query_params.get('user_id')
        _type  = self.request.query_params.get('note_type')
        if appointment_id:
            queryset = queryset.filter(consultation__appointment_id=appointment_id)
        else:
            # Filter by the request user (assuming `user_id` field in `SavedNote` model)
            # Adjust the field name if your model uses a different field for the user
            queryset = queryset.filter(user_id=self.request.user.id,note_type = _type)

        return queryset
    

class UserSavedNoteViewSet(viewsets.ModelViewSet): 
    queryset            = SavedNote.objects.all()
    serializer_class    = SavedNoteSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_fields    = ['consultation_id','note_type',]
    def get_queryset(self):
        queryset        = SavedNote.objects.all()
        appointment_id  = self.request.query_params.get('appointment_id')
        _type  = self.request.query_params.get('note_type')
        print(self.request.query_params)
        if appointment_id:
            try:
                consultation = Consultation.objects.get(appointment_id=appointment_id)
                queryset = queryset.filter(consultation_id=consultation.id)
            except Consultation.DoesNotExist:
                # Handle case where no consultation is found for the provided appointment ID
                queryset = SavedNote.objects.none()
        else:
            doctor = self.request.user
            print(doctor)
            queryset = queryset.filter(user_id=doctor.id,note_type = _type)

        return queryset

class AddNoteView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
