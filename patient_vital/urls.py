from rest_framework.routers import SimpleRouter
from .views import PatientVitalViewSet , SelfPatientVitalView
from django.urls import path, include


router = SimpleRouter()
router.register('', PatientVitalViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('self/', SelfPatientVitalView.as_view(), name='user_specialization_mapping'),
    path('', include(router.urls)),
    
]