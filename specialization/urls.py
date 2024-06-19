from django.urls import path
from .views import SpecializationDetail, SpecializationList

urlpatterns = [
    path('',SpecializationList.as_view()),
    path('<int:pk>/',SpecializationDetail.as_view()),
    #New Path to be added hereby -->
    
    ]