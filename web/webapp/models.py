from django.db import models
from django.utils import timezone

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    firstUser = models.BooleanField(default=False)
    botAnswer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Conversation with {self.username}"
