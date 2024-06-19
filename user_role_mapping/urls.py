from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import UserRoleMappingViewSet , MappingRoleForSessionUser


router = SimpleRouter()
router.register('', UserRoleMappingViewSet, basename='user-role-mapping')

urlpatterns = [
    path('add/', MappingRoleForSessionUser.as_view(), name='session_user-role-mapping'),
    
    path('', include(router.urls)),
]