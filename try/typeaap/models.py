from django.contrib.auth.models import AbstractUser
from django.db import models
class UserProfile(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    wpm = models.FloatField(default=0)  # Words Per Minute (WPM) score
    accuracy = models.IntegerField(default=0.0)

def save(self, *args, **kwargs):
        # Set default values if not provided
        if self.pk is None:
            self.wpm = 0
            self.accuracy = 0.0
        super(UserProfile, self).save(*args, **kwargs)