from django.conf import settings
from django.db import models


class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('UPDATE_CREATED', 'Update Created'),
        ('COMMENT_ADDED', 'Comment Added'),
        ('REACTION_ADDED', 'Reaction Added'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    action = models.CharField(max_length=50, choices=ACTION_CHOICES)

    update = models.ForeignKey(
        'updates.Update',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    metadata = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.action}"