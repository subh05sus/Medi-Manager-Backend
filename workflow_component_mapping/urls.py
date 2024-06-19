from rest_framework.routers import SimpleRouter
from .views import WorkflowComponentMappingViewSet 


router = SimpleRouter()
router.register('', WorkflowComponentMappingViewSet,)
urlpatterns = router.urls