from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import VisitorContactViewSet 


router = SimpleRouter()
router.register('', VisitorContactViewSet)

urlpatterns = [
    # path('self/', AdvUserReferDoctorView.as_view(), name='user_specialization_mapping'),
    path('', include(router.urls)),
]