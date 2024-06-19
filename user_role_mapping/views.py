from .models import UserRoleMapping
from .serializers import UserRoleMappingSerializer
from rest_framework import viewsets , status

from rest_framework.views import APIView
from rest_framework.response import Response
from role.models import Role

# Create your views here.

class UserRoleMappingViewSet(viewsets.ModelViewSet): # new
    queryset = UserRoleMapping.objects.all()
    serializer_class = UserRoleMappingSerializer

class MappingRoleForSessionUser(APIView):
    def post(self, request):
        user = self.request.user

        request_data = request.data
        role_id = request_data.get('role_id', None)
        
        # Checking if the role_id is provided
        if role_id is None:
            return Response({'error': 'Role ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Checking if the role with the provided role_id exists
            role_instance = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return Response({'error': 'Role with the provided ID does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        data = {'user_id': user.id, 'role_id': role_instance}
    
        serializer = UserRoleMappingSerializer(data=data)
        
        # Validating and saving serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)