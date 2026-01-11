from django.db import models
from users.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organized_events"
    )

    participants = models.ManyToManyField(
        User,
        related_name="attended_events",
        blank=True
    )

    capacity = models.PositiveIntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_time"]
        indexes = [
            models.Index(fields=["start_time"]),
            models.Index(fields=["location"]),
        ]

    def __str__(self):
        return self.title


