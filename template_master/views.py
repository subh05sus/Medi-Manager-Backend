from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from .models import TemplateMaster
from .serializers import TemplateMasterSerializer,GeneralTemplateMasterSerializer

from .serializers import (GeneralTemplateMasterSerializer, 
                          TemplateMasterWithMedicineSerializer, 
                          TemplateMasterWithInvestigationSerializer)

# Create your views here.

class TemplateMasterViewSet(viewsets.ModelViewSet): # new
    queryset = TemplateMaster.objects.all()
    serializer_class = GeneralTemplateMasterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'template_type',]
    
    def get_serializer_class(self):
        print('retrive action')
        if self.action == 'retrieve':
            instance = self.get_object()
            if instance.template_type == 'MS':
                print('Medicine data to be fetchd')
                print(TemplateMasterWithMedicineSerializer.data)
                return TemplateMasterWithMedicineSerializer
            elif instance.template_type == 'IS':
                return TemplateMasterWithInvestigationSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')

        # If 'user_id' is not explicitly provided in the query parameters, 
        # filter by the current session user
        if not user_id:
            queryset = queryset.filter(user_id=self.request.user)


        return queryset


@api_view(['GET', 'POST'])
def template_master_list_create(request):
    if request.method == 'GET':
        print('USER == ',request.user)
        template_type = request.query_params.get('template_type')
        if template_type:
            templates = TemplateMaster.objects.filter(template_type=template_type,user_id=request.user)
        else:
            templates = TemplateMaster.objects.filter(user_id=request.user)
        serializer = TemplateMasterSerializer(templates, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['user_id'] = request.user.id
        print(request.data)

        serializer = TemplateMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
