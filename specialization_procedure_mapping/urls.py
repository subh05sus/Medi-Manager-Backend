from rest_framework.routers import SimpleRouter
from .views import SpecializationProcedureMappingViewSet 


router = SimpleRouter()
router.register('', SpecializationProcedureMappingViewSet,)
urlpatterns = router.urls