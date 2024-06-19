from rest_framework.routers import SimpleRouter
from .views import SpecializationWorkflowMappingViewSet 


router = SimpleRouter()
router.register('', SpecializationWorkflowMappingViewSet,)
urlpatterns = router.urls