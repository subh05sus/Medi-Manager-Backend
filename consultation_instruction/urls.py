from rest_framework.routers import SimpleRouter
from .views import ConsultationInstructionViewSet , AddConsultatioInstructionView
from django.urls import include , path


router = SimpleRouter()
router.register('', ConsultationInstructionViewSet, basename='consultation-instruction-set')

urlpatterns = [
    path('add/', AddConsultatioInstructionView.as_view(), name='consultation-medicine'),
    # path('list/', ConsultationSymptomListView.as_view(), name='consultation-symptom-list'),
    # Include router urls
    path('', include(router.urls)),
]
