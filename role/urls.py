from django.urls import path
from .views import RoleList,RoleDetail

urlpatterns = [
    path('',RoleList.as_view()),
    path('<int:pk>/',RoleDetail.as_view()),
    # New Path to be added hereby -->
    ]