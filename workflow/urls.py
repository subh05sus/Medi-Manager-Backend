from rest_framework.routers import SimpleRouter
from .views import WorkflowViewSet 


router = SimpleRouter()
router.register('', WorkflowViewSet,)
urlpatterns = router.urls