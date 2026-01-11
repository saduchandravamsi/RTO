from django.db import models
from django.contrib.auth.models import User
from apps.slots.models import DrivingTestSlot


class DrivingTestSession(models.Model):

    RESULT_CHOICES = [
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    ]

    slot = models.OneToOneField(
        DrivingTestSlot,
        on_delete=models.CASCADE,
        related_name='test_session'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='driving_test_sessions'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    final_result = models.CharField(
        max_length=4,
        choices=RESULT_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - Session {self.id}"
