from rest_framework.routers import SimpleRouter
from .views import ProcedureViewSet 


router = SimpleRouter()
router.register('', ProcedureViewSet,)
urlpatterns = router.urls