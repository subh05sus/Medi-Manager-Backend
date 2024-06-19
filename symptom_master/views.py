from .models import SymptomMaster
from .serializers import SymptomMasterSerializer
from rest_framework import viewsets # new

# Create your views here.

class SymptomMasterViewSet(viewsets.ModelViewSet): # new
    queryset = SymptomMaster.objects.all()
    serializer_class = SymptomMasterSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import SymptomMasterListSerializer

# class SymptomMasterListView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = SymptomMasterListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Symptoms added successfully."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
