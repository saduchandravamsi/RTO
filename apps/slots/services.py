from datetime import timedelta
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from .models import DrivingTestSlot
from .serializers import DrivingTestSlotSerializer


class SlotService:

    @staticmethod
    def book_slot(user, data):

        # 1️⃣ Check active booking
        active_slot = DrivingTestSlot.objects.filter(
            user=user,
            slot_status='BOOKED'
        ).exists()

        if active_slot:
            raise ValidationError("You already have an active slot booked.")

        # 2️⃣ Check last completed slot (30 days rule)
        last_completed_slot = DrivingTestSlot.objects.filter(
            user=user,
            slot_status='COMPLETED'
        ).order_by('-completed_at').first()

        if last_completed_slot and last_completed_slot.completed_at:
            if timezone.now() < last_completed_slot.completed_at + timedelta(days=30):
                raise ValidationError(
                    "You can book a new slot only after 30 days from last test."
                )

        # 3️⃣ Allow booking
        serializer = DrivingTestSlotSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        slot = serializer.save(user=user)

        return {
            "message": "Slot booked successfully",
            "slot_id": slot.id
        }
class SlotService:

    @staticmethod
    def get_my_bookings(user):
        slots = DrivingTestSlot.objects.filter(user=user).order_by('-created_at')
        return slots
