from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import TemplateMasterViewSet ,template_master_list_create


router = SimpleRouter()
router.register('', TemplateMasterViewSet,)
urlpatterns = [
    path('detail/', template_master_list_create, name='template-master-list-create'),
    path('', include(router.urls)),
]


