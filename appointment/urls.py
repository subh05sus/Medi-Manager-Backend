from django.urls import path,include
from .views import AppointmentDetail , patient_latest_appointments_view
from .views import UserAppointmentsView , AppointmentCreateView, AppointmentCreateForPatient, AppointmentSummaryView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# router.register('', AppointmentList,basename='consultation')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/',AppointmentDetail.as_view()),
    #New Path to be added hereby -->
    path('doctor_specific/',    UserAppointmentsView.as_view(),     name='user-appointments'),
    path('report/',             AppointmentSummaryView.as_view(),   name='aggregrated_appointments'),
    
    path('create/',             AppointmentCreateForPatient.as_view(), name='patient-appointments'),
    path('add/',                AppointmentCreateView.as_view(),    name='create-appointments'),
    path('patient-latest/',     patient_latest_appointments_view,     name='user-appointments'),
    
    ]

