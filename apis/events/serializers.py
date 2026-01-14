from django.utils import timezone
from rest_framework import serializers
from events.models import Event
from apis.users.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
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
        read_only_fields = ["organizer", "participants"]

    def validate(self, data):
        start = data.get("start_time")
        end = data.get("end_time")

        if start and end and end <= start:
            raise serializers.ValidationError(
                {"end_time": "End time must be after start time"}
            )

        if start and start < timezone.now():
            raise serializers.ValidationError(
                {"start_time": "Event cannot start in the past"}
            )

        return data

