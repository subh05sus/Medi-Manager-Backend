from rest_framework.routers import SimpleRouter
from .views import ComponentViewSet 


router = SimpleRouter()
router.register('', ComponentViewSet,)
urlpatterns = router.urls