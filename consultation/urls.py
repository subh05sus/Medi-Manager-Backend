from rest_framework.routers import SimpleRouter
from .views import ConsultationViewSet , ConsultationAPIView , ConsultationCreateView , ConsultationPrescriptionViewSet, ConsultationFindingViewSet , PrescriptionPrintView, get_prescription_pdf
from django.urls import path, include


router = SimpleRouter()
router.register('', ConsultationViewSet,basename='consultation')
# router.register('query/', ConsultationFindingViewSet,basename='consultation-finding')
# router.register('prp/', ConsultationPrescriptionViewSet, basename='consultation-data-set')
urlpatterns = [
    path('add/', ConsultationAPIView.as_view(), name='consultation-symptoms'),
    path('create/', ConsultationCreateView.as_view(), name='consultation-check'),
    path('query/', ConsultationFindingViewSet.as_view({'get': 'list'}), name='consultation-finding-list'),
    path('rx/', ConsultationPrescriptionViewSet.as_view({'get': 'list'}), name='consultation-prescriptions-list'),
    path('rx-print/', PrescriptionPrintView.as_view({'post': 'create'}), name='consultation-prescriptions-print'),
    # path('consultations/prescriptions/print/', PrescriptionPrintView.as_view({'post': 'create'}), name='consultation-prescriptions-print'),
    path('prescriptions/<int:appointment_id>/', get_prescription_pdf, name='prescription_pdf'),

    # Include router urls
    path('', include(router.urls)),
    
]
