from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.email