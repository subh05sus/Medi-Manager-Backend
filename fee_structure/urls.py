from django.urls import path , include
from rest_framework.routers import SimpleRouter
from .views import UserFeeStructureForSessionUser , UserFeeStructureViewSet,  UpdateUserFeeStructure, \
                    CreateBulkUserFeeStructure , FeeTypeViewSet 


router = SimpleRouter()
router.register('', FeeTypeViewSet, basename='user-fee-mapping'),
router.register('fee_type/', FeeTypeViewSet, basename='all-fee-types')

urlpatterns = [
    path('self/',   UserFeeStructureForSessionUser.as_view(), name='session_user-fee-type-mapping'),
    path('update/<int:pk>/', UpdateUserFeeStructure.as_view(), name='update-user-fee-structure'),
    path('add/',    CreateBulkUserFeeStructure.as_view(), name='bulk-create-fee-structure'),
    path('',        include(router.urls)),
]

