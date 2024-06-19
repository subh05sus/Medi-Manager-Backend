from .models import UserSpecializationProcedureMapping
from .serializers import UserSpecializationProcedureMappingSerializer , GetUserSpecializationProcedureMappingSerializer
from rest_framework import viewsets # new
from rest_framework.views import APIView
from specialization.models import Specialization
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class UserSpecializationProcedureMappingViewSet(viewsets.ModelViewSet): 
    queryset = UserSpecializationProcedureMapping.objects.all()
    serializer_class = UserSpecializationProcedureMappingSerializer


class AdvUserSpecializationProcedureMappingView(APIView):
    def get(self, request, *args, **kwargs):
        session_user = request.user
        mappings = UserSpecializationProcedureMapping.objects.filter(user_id=session_user.id)
        serializer = GetUserSpecializationProcedureMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        session_user = request.user
        request_data = request.data.copy()
        request_data['user_id'] = session_user.id
        specialization_name = request_data.pop('specialization_name', None)
        if specialization_name:
            specialization, _ = Specialization.objects.get_or_create(name__iexact=specialization_name,
                                                                     defaults={'name': specialization_name.capitalize()})
            request_data['specialization_id'] = specialization.id
            print(request_data)

        serializer = UserSpecializationProcedureMappingSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




