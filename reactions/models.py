from django.conf import settings
from django.db import models


class Reaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reactions'
    )

    update = models.ForeignKey(
        'updates.Update',
        on_delete=models.CASCADE,
        related_name='reactions'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'update')

    def __str__(self):
        return f"{self.user.email} liked update {self.update.id}"