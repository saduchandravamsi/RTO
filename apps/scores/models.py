from django.db import models
from apps.test_sessions.models import DrivingTestSession


class TestScore(models.Model):

    DECISION_CHOICES = [
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    ]

    session = models.OneToOneField(
        DrivingTestSession,
        on_delete=models.CASCADE,
        related_name='test_score'
    )
    lane_score = models.IntegerField()
    parking_score = models.IntegerField()
    signal_score = models.IntegerField()
    total_score = models.IntegerField()
    decision = models.CharField(
        max_length=4,
        choices=DECISION_CHOICES
    )

    def __str__(self):
        return f"Session {self.session.id} - {self.decision}"
