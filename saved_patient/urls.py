from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import SavedPatientViewSet , SavedPatientForSessionUser , SavedPatientView


router = SimpleRouter()
router.register('', SavedPatientViewSet, basename='doctor-savedpatient-mapping')

urlpatterns = [
    path('add/', SavedPatientForSessionUser.as_view(), name='session_user-patient-mapping'),
    path('self/', SavedPatientView.as_view(), name='all-saved-patient'),
    path('', include(router.urls)),
]