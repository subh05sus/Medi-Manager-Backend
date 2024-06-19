from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InvestigationMasterViewSet 


router = SimpleRouter()
router.register('', InvestigationMasterViewSet,)
urlpatterns = router.urls