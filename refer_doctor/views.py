from .models import ReferDoctor
from specialization.models import Specialization
from .serializers import ReferDoctorSerializer
from rest_framework import viewsets # new

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class  UserReferDoctorViewSet(viewsets.ModelViewSet): 
    queryset = ReferDoctor.objects.all()
    serializer_class = ReferDoctorSerializer
    # def create(self, request, *args, **kwargs):
    #     user_id = request.data.get('user_id', None)
    #     if not user_id:
    #         user_id = request.user.id
    #     specialization_name = request.data.pop('specialization_name', None)
    #     if specialization_name:
    #         specialization, _ = Specialization.objects.get_or_create(name=specialization_name)
        #     request.data['specialization_id'] = specialization.id

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class AdvUserReferDoctorView(APIView):
    def get(self, request, *args, **kwargs):
        session_user = request.user
        mappings = ReferDoctor.objects.filter(user_id=session_user.id)
        serializer = ReferDoctorSerializer(mappings, many=True)
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

        serializer = ReferDoctorSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)