from django.db import models
from django.contrib.auth.models import User


class DrivingTestSlot(models.Model):

    SLOT_STATUS_CHOICES = [
        ('BOOKED', 'Booked'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='driving_test_slots'
    )
    test_date = models.DateField()
    test_time = models.TimeField()
    rto_location = models.CharField(max_length=100)
    slot_status = models.CharField(
        max_length=10,
        choices=SLOT_STATUS_CHOICES,
        default='BOOKED'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test_date} {self.test_time}"
