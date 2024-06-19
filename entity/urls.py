from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import EntityViewSet 


router = SimpleRouter()
router.register('', EntityViewSet,)
urlpatterns = router.urls