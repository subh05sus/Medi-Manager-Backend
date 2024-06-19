from rest_framework.routers import SimpleRouter
from .views import EntityTypeViewSet 


router = SimpleRouter()
router.register('', EntityTypeViewSet,)
urlpatterns = router.urls