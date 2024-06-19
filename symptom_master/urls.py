from rest_framework.routers import SimpleRouter
from .views import SymptomMasterViewSet 


router = SimpleRouter()
router.register('', SymptomMasterViewSet,)
urlpatterns = router.urls

# from django.urls import path
# from .views import SymptomMasterListView

# urlpatterns = [
#     path('', SymptomMasterListView.as_view(), name='symptom-master-list'),
# ]
