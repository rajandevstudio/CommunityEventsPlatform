from django.utils import timezone
from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source="organizer.username")
    participants = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "start_time",
            "end_time",
            "location",
            "capacity",
            "organizer",
            "participants",
        ]

    def validate(self, data):
        if data["start_time"] >= data["end_time"]:
            raise serializers.ValidationError(
                "End time must be after start time"
            )

        if data["start_time"] < timezone.now():
            raise serializers.ValidationError(
                "Event cannot start in the past"
            )

        return data
