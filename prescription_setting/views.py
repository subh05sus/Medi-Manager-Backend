from rest_framework import viewsets
from .models import PrescriptionSetting
from .serializers import PrescriptionSettingSerializer

class PrescriptionSettingViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionSetting.objects.all()
    serializer_class = PrescriptionSettingSerializer

    def get_queryset(self):
        return PrescriptionSetting.objects.filter(doctor_id=self.request.user)
    def perform_create(self, serializer):
        serializer.save(doctor_id=self.request.user)
