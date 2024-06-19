from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserEntityMappingViewSet 


router = SimpleRouter()
router.register('', UserEntityMappingViewSet,)
urlpatterns = router.urls