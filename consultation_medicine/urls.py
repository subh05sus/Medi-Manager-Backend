from rest_framework.routers import SimpleRouter
from .views import ConsultationMedicineViewSet , AddConsultationMedicineView
from django.urls import include , path


router = SimpleRouter()
router.register('', ConsultationMedicineViewSet, basename='consultation-symptom-set')



# Define your urlpatterns
urlpatterns = [
    path('add/', AddConsultationMedicineView.as_view(), name='consultation-medicine'),
    # path('list/', ConsultationSymptomListView.as_view(), name='consultation-symptom-list'),
    # Include router urls
    path('', include(router.urls)),
]
