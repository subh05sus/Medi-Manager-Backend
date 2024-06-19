from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MedicineMasterViewSet 


router = SimpleRouter()
router.register('', MedicineMasterViewSet,)
urlpatterns = router.urls