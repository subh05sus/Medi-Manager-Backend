from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserSpecializationProcedureMappingViewSet,  AdvUserSpecializationProcedureMappingView

router = SimpleRouter()
router.register('', UserSpecializationProcedureMappingViewSet)

urlpatterns = [
    path('self/', AdvUserSpecializationProcedureMappingView.as_view(), name='user_specialization_mapping'),
    path('', include(router.urls)),
    
]
