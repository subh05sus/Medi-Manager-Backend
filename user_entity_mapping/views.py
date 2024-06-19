from .models import UserEntityMapping
from .serializers import UserEntityMappingSerializer
from rest_framework import viewsets # new
from entity.models import Entity
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class  UserEntityMappingViewSet(viewsets.ModelViewSet): # new
    queryset = UserEntityMapping.objects.all()
    serializer_class = UserEntityMappingSerializer
    def create(self, request, *args, **kwargs):
        # If user_id is not provided, get it from session user
        user_id = request.data.get('user_id', None)
        if not user_id:
            # Assuming your session user is stored in request.user
            user_id = request.user.id

        # Get or create Entity based on provided entity_name
        entity_name = request.data.pop('entity_name', None)
        if entity_name:
            entity, _ = Entity.objects.get_or_create(name=entity_name)
            request.data['entity_id'] = entity.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)