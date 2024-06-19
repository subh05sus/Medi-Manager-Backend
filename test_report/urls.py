from rest_framework.routers import SimpleRouter
from .views import TestReportViewSet 


router = SimpleRouter()
router.register('', TestReportViewSet)
urlpatterns = router.urls