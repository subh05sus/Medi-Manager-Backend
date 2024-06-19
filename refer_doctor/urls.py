from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import UserReferDoctorViewSet , AdvUserReferDoctorView


router = SimpleRouter()
router.register('', UserReferDoctorViewSet)

urlpatterns = [
    path('self/', AdvUserReferDoctorView.as_view(), name='user_specialization_mapping'),
    path('', include(router.urls)),
]