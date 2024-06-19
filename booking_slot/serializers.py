from rest_framework import serializers
from .models import BookingSlotConfig , Slot , DayGroup


class BookingSlotConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingSlotConfig
        fields = [
            'day',
            'is_active',
            'morning_slots_is_active', 'morning_start_time', 'morning_end_time', 'morning_slots',
            'afternoon_slots_is_active', 'afternoon_start_time', 'afternoon_end_time', 'afternoon_slots',
            'evening_slots_is_active', 'evening_start_time', 'evening_end_time', 'evening_slots'
        ]

class DayGroupSerializer(serializers.ModelSerializer):
    booking_config_list = BookingSlotConfigSerializer(many=True, source='booking_slots')

    class Meta:
        model = DayGroup
        fields = ['name','is_active', 'booking_config_list']

    def create(self, validated_data):
        booking_configs_data = validated_data.pop('booking_slots')
        day_group, _ = DayGroup.objects.get_or_create(
            name=validated_data['name'],
            defaults={'doctor_id': self.context['request'].user}
        )
        if validated_data.get('is_active'):
            day_group.is_active = validated_data['is_active']
            day_group.save()
        print(day_group)
        for booking_config_data in booking_configs_data:
            booking_config_data['day_group'] = day_group
            BookingSlotConfig.objects.create(**booking_config_data)

        return day_group






class SlotSerializer(serializers.ModelSerializer):
    booking_slot_day = serializers.CharField(source='booking_slot.day', read_only=True)

    class Meta:
        model = Slot
        fields = ['id', 
                  'date',
                  'booking_config_id', 
                  'booking_slot_day', 
                  'session_type', 
                  'slot_number', 
                  'is_booked']



class BookedSlotsSerializer(serializers.Serializer):
    active_config = serializers.CharField()
    slot_config_id  = serializers.IntegerField()
    total_slots     = serializers.IntegerField()
    booked_slot_list= serializers.ListField(child=serializers.IntegerField())
    

