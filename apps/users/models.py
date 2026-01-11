from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    mobile_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='user_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
