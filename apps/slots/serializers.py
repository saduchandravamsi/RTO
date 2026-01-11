from rest_framework import serializers
from .models import DrivingTestSlot


class DrivingTestSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrivingTestSlot
        fields = ['test_date', 'test_time', 'rto_location']

class MyBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrivingTestSlot
        fields = [
            'id',
            'test_date',
            'test_time',
            'rto_location',
            'slot_status',
            'created_at',
            'completed_at'
        ]
