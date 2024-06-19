from django.urls import path , include
from rest_framework.routers import SimpleRouter

from .views import DoctorLeaveListCreate , AppliedLeaveViewSet


router = SimpleRouter()
router.register('', AppliedLeaveViewSet, basename='all-fee-types')

urlpatterns = [
    path('', include(router.urls)),
    path('self/', DoctorLeaveListCreate.as_view(), name='doctor-leave-list-create'),
]

