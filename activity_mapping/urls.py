from rest_framework.routers import SimpleRouter
from .views import ActivityMappingViewSet 


router = SimpleRouter()
router.register('', ActivityMappingViewSet,)
urlpatterns = router.urls