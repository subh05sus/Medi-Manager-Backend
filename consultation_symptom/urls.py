from django.urls import path, include
from .views import ConsultationSymptomView, ConsultationSymptomListView 
from rest_framework.routers import SimpleRouter

# Set up the router and register your viewsets
router = SimpleRouter()
router.register('', ConsultationSymptomListView, basename='consultation-symptom-set')

# Define your urlpatterns
urlpatterns = [
    path('add/', ConsultationSymptomView.as_view(), name='consultation-symptoms'),
    # path('fingerprint/', ConsultationSymptomFingerprintView, name='consultation-symptom-set'),
    # Include router urls
    path('', include(router.urls)),
]
