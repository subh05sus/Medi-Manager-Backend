from .models import UserFeeStructure , FeeType
from .serializers import UserFeeStructureSerializer , FeeTypeSerializer
from rest_framework import viewsets , status
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from django_filters import rest_framework as filters

from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from django.db import IntegrityError





# Create your views here.

class FeeTypeFilter(filters.FilterSet):
    # cost_type = filters.CharFilter(field_name='cost_type')
    class Meta:
        model = FeeType
        fields = ['cost_type']

class FeeTypeViewSet(viewsets.ModelViewSet):
    queryset = FeeType.objects.all()
    serializer_class = FeeTypeSerializer
    filter_backends     = [DjangoFilterBackend]
    filterset_class = FeeTypeFilter

class UserFeeStructureViewSet(viewsets.ModelViewSet):
    queryset            = UserFeeStructure.objects.all()
    serializer_class    = UserFeeStructureSerializer



class UserFeeStructureForSessionUser(ListCreateAPIView):
    serializer_class    = UserFeeStructureSerializer
    
    def get_queryset(self):
        user = self.request.user
        print(user)
        return UserFeeStructure.objects.filter(user_id=user.id)
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        request_data = request.data.copy()

        fee_type_name = request_data.get('fee_type_name', None)
        c_type = request_data.get('cost_type')
        if fee_type_name:
            if c_type:
                fee_type, _ = FeeType.objects.get_or_create(name=fee_type_name , cost_type = c_type)
            else:
                fee_type, _ = FeeType.objects.get_or_create(name=fee_type_name)
            request_data['fee_type'] = fee_type.id

        else:
            return Response({"error": "fee_type_name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        request_data['user_id'] = user.id

        serializer = self.get_serializer(data=request_data)
        fee_structure, _ = UserFeeStructure.objects.get_or_create(
                    user_id=user, fee_type=fee_type,
                )
                # If not created, it means it exists, so we update the fee amount
       
        fee_structure.fee_amount = request_data['fee_amount']
        fee_structure.save()
        instance_data = {
            'id': fee_structure.id,
            'user_id': fee_structure.user_id.id,
            'fee_type': fee_structure.fee_type.id,
            'fee_amount': fee_structure.fee_amount,
            'fee_type_name': fee_type.name,
                'cost_type' : fee_type.cost_type
        }
        
        if serializer.is_valid():
            return Response(instance_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied



class UpdateUserFeeStructure(GenericAPIView):
    serializer_class = UserFeeStructureSerializer

    def get_object(self):
        instance_id = self.kwargs.get('pk')
        try:
            instance = UserFeeStructure.objects.get(pk=instance_id)
        except UserFeeStructure.DoesNotExist:
            raise NotFound('No fee structure found with this ID.')

        # Ensure that the user has permission to update this instance
        if instance.user_id != self.request.user:
            raise PermissionDenied('You do not have permission to update this fee structure.')
        
        return instance

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        request_data = request.data.copy()

        fee_type_name = request_data.get('fee_type_name', None)
        if fee_type_name:
            fee_type, _ = FeeType.objects.get_or_create(name=fee_type_name)
            request_data['fee_type'] = fee_type.id

        serializer = self.serializer_class(instance, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreateBulkUserFeeStructure(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data  # This should be a list of dictionaries
        c_type = 'DF'

        if not isinstance(data, list):
            return Response({"error": "Expected a list of fee structures"}, status=status.HTTP_400_BAD_REQUEST)

        created_instances = []
        errors = []

        for item in data:
            fee_type_name = item.get('fee_type_name')
            fee_amount = item.get('fee_amount')
            cost_type = item.get('cost_type')

            if cost_type is not None:
                c_type = cost_type

            if not fee_type_name or fee_amount is None:
                errors.append({"error": "Missing fee_type_name or fee_amount", "item": item})
                continue

            # Ensure fee_type exists or create new one with a default cost type
            fee_type, _ = FeeType.objects.get_or_create(name=fee_type_name, cost_type = c_type)

            try:
                # Attempt to get or create the UserFeeStructure instance
                fee_structure, _ = UserFeeStructure.objects.get_or_create(
                    user_id=user, fee_type=fee_type,
                )
                # If not created, it means it exists, so we update the fee amount
        
                fee_structure.fee_amount = fee_amount
                fee_structure.save()
                instance_data = {
                    'id': fee_structure.id,
                    'user_id': fee_structure.user_id.id,
                    'fee_type': fee_structure.fee_type.id,
                    'fee_amount': fee_structure.fee_amount,
                    'fee_type_name': fee_type.name,
                     'cost_type' : fee_type.cost_type,
                    'created': _  # This indicates if the instance was newly created
                }
                created_instances.append(instance_data)
            except IntegrityError as e:
                errors.append({"error": str(e), "item": item})

        if errors:
            return Response({"errors": errors, "created": created_instances}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"created": created_instances}, status=status.HTTP_201_CREATED)
