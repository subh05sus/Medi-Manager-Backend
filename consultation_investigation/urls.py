from rest_framework.routers import SimpleRouter
from .views import ConsultationInvestigationViewSet  , AddConsultationInvestigationView
from django.urls import path , include


router = SimpleRouter()
router.register('', ConsultationInvestigationViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('add/', AddConsultationInvestigationView.as_view(), name='consultation-medicine'),
    # path('list/', ConsultationSymptomListView.as_view(), name='consultation-symptom-list'),
    # Include router urls
    path('', include(router.urls)),
]