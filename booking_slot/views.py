from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .models import BookingSlotConfig , Slot , DayGroup
from .serializers import BookingSlotConfigSerializer  , BookedSlotsSerializer , DayGroupSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

# views.py



class BookingSlotListCreate(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DayGroupSerializer  
        return DayGroupSerializer  

    def get_queryset(self):
        daygroup_for_user = DayGroup.objects.filter(doctor_id=self.request.user)
        daygroup_ids = daygroup_for_user.values_list('id', flat=True)
        return DayGroup.objects.filter(id__in=daygroup_ids)

    def perform_create(self, serializer):
        if isinstance(serializer, DayGroupSerializer):
            serializer.save(doctor_id=self.request.user)  # Ensure the doctor is set correctly when saving the DayGroup
        else:
            super().perform_create(serializer)



class BookedSlotsAPIView(APIView):

    def get(self, request, format=None):
        date_str = request.query_params.get('date')
        session_type = request.query_params.get('session')

        if not date_str or not session_type:
            return Response({'error': 'Date and session parameters are required.'}, status=400)
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            weekday = date.strftime('%a').lower()  
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
        user_daygroups = DayGroup.objects.filter(doctor_id=self.request.user , is_active=True)
        active_daygroup = user_daygroups.first()

        booking_slots = BookingSlotConfig.objects.filter(
            day_group = active_daygroup, 
            day       = weekday)
 
        # Check if the booking slot exists
        if not booking_slots.exists():
            return Response({'error': 'No booking slots found for this date.'}, status=404)
        booking_slot = booking_slots.first()

        booked_slots = Slot.objects.filter(
                        session_type=session_type, 
                        booking_config_id = booking_slot ,
                        is_booked=True ).values_list('slot_number', flat=True)
        total_booking_slots = booking_slot.get_slots_for_session('morning')
        # Serialize the data
        serializer = BookedSlotsSerializer({'active_config'    : active_daygroup.name,
                                            'slot_config_id'    : booking_slot.id,
                                            'total_slots'       : total_booking_slots,
                                            'booked_slot_list'  : booked_slots})
        return Response(serializer.data)
    




class CreateSlotAPIView(APIView):

    def post(self, request, format=None):
        date_str = request.data.get('date')
        session_type = request.data.get('session')
        slot_number = request.data.get('slot_number')


        if not date_str or not session_type or slot_number is None:
            return Response({'error': 'Date, session type, and slot number parameters are required.'}, status=400)

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            weekday = date.strftime('%a').lower()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        try:
            booking_slot_config = BookingSlotConfig.objects.get(
                doctor_id=request.user,
                day=weekday
            )
        except BookingSlotConfig.DoesNotExist:
            return Response({'error': 'No booking slot configuration found for this date and doctor.'}, status=404)

        # Check if the slot is already booked
        if Slot.objects.filter(booking_config_id=booking_slot_config, slot_number=slot_number, session_type=session_type).exists():
            return Response({'error': 'The slot is already booked.'}, status=400)

        new_slot = Slot(
            date        =date,
            session_type=session_type,
            slot_number=slot_number,
            booking_config_id=booking_slot_config,
            is_booked=True
        )
        new_slot.save()

        return Response({'message': 'The slot has been successfully booked.', 'slot_id': new_slot.id})

  

