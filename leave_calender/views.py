from .models import AppliedLeave
from .serializers import AppliedLeaveSerializer 
from rest_framework import viewsets , status

from rest_framework.generics import ListCreateAPIView
from django_filters import rest_framework as filters
from rest_framework import generics
from django.db.models import Q



class AppliedLeaveViewSet(viewsets.ModelViewSet):
    queryset = AppliedLeave.objects.all()
    serializer_class = AppliedLeaveSerializer
    # filter_backends     = [DjangoFilterBackend]
    # filterset_class     = FeeTypeFilter


class DoctorLeaveListCreate(generics.ListCreateAPIView):
    serializer_class = AppliedLeaveSerializer

    def get_queryset(self):
        queryset = AppliedLeave.objects.filter(user_id=self.request.user)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            # Filter leaves that overlap with the provided date range
            queryset = queryset.filter(
                Q(startDate__lte=end_date) & Q(endDate__gte=start_date)
            )
        return queryset
        

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
