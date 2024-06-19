# urls.py
from django.urls import path
from .views import BookingSlotListCreate, BookedSlotsAPIView , CreateSlotAPIView

urlpatterns = [
    path('self/', BookingSlotListCreate.as_view(), name='booking-slot-list-create'),
    path('booked_slots/', BookedSlotsAPIView.as_view(), name='booked-slots'),
    path('book_slot/', CreateSlotAPIView.as_view(), name='create-slot'),
]

