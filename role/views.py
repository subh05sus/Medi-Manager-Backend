from rest_framework import generics
from .models import Role
from .serializers import RoleSerializer

# Create your views here.

class RoleList(generics.ListCreateAPIView):
    queryset            = Role.objects.all()
    serializer_class    = RoleSerializer
class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset        = Role.objects.all()
    serializer_class = RoleSerializer
