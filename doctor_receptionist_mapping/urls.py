from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import DoctorReceptionistMappingViewSet , MappingReceptionistForSessionUser , UserReceptionistView


router = SimpleRouter()
router.register('', DoctorReceptionistMappingViewSet, basename='user-receptionist-mapping')

urlpatterns = [
    path('add/', MappingReceptionistForSessionUser.as_view(), name='session_user-receptionist-mapping'),
    path('self/', UserReceptionistView.as_view(), name='user-receptionist'),
    path('', include(router.urls)),
]