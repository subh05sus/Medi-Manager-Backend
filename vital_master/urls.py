from rest_framework.routers import SimpleRouter
from .views import VitalMasterViewSet 


router      = SimpleRouter()
router.register('', VitalMasterViewSet)
urlpatterns = router.urls