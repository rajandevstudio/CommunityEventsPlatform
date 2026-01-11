from apis.events.filters import EventFilter
from apis.events.serializers import EventSerializer
from events.models import Event
from rest_framework.permissions import IsAuthenticated
from apis.events.permissions import IsOrganizer, IsEventOwner
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiResponse,
)



@extend_schema_view(
    list=extend_schema(
        summary="List events",
        description="Get a list of all events",
        responses={200: EventSerializer(many=True)},
        tags=["Events"]
    ),
    retrieve=extend_schema(
        summary="Retrieve event",
        description="Get event details by ID",
        responses={200: EventSerializer},
        tags=["Events"]
    ),
    create=extend_schema(
        summary="Create event",
        description="Create a new event (Organizer only)",
        request=EventSerializer,
        responses={201: EventSerializer},
        tags=["Events"]
    ),
    update=extend_schema(
        summary="Update event",
        description="Update an event (Organizer & Owner only)",
        request=EventSerializer,
        responses={200: EventSerializer},
        tags=["Events"]
    ),
    partial_update=extend_schema(
        summary="Partially update event",
        description="Partially update an event",
        request=EventSerializer,
        responses={200: EventSerializer},
        tags=["Events"]
    ),
    destroy=extend_schema(
        summary="Delete event",
        description="Delete an event (Organizer & Owner only)",
        responses={204: OpenApiResponse(description="Deleted successfully")},
        tags=["Events"]
    ),

)
class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EventFilter
    ordering_fields = ["start_time", "created_at"]
    ordering = ["start_time"]

    def get_queryset(self):
        return Event.objects.all()

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated(), IsOrganizer()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOrganizer(), IsEventOwner()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


    @extend_schema(
        summary="Join an event",
        description=(
            "Allows an authenticated user to join an event.\n\n"
            "**Rules:**\n"
            "- Organizer cannot join their own event\n"
            "- User cannot join twice\n"
            "- Event must have available capacity"
        ),
        responses={
            200: OpenApiResponse(
                description="Joined successfully",
                examples=[
                    {"message": "Joined successfully"}
                ],
            ),
            400: OpenApiResponse(
                description="Invalid join attempt",
                examples=[
                    {"message": "Organizer cannot join their own event"},
                    {"message": "User already joined"},
                    {"message": "Event is full"},
                ],
            ),
            401: OpenApiResponse(description="Authentication required"),
        },
        tags=['Events']
    )
    @action(detail=True, methods=["post"], url_path="join")
    def join_event(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if user == event.organizer:
            return Response(
                {"message": "Organizer cannot join their own event"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if event.participants.filter(id=user.id).exists():
            return Response(
                {"message": "User already joined"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if event.participants.count() >= event.capacity:
            return Response(
                {"message": "Event is full"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
            event.participants.add(user)

        return Response(
            {"message": "Joined successfully"},
            status=status.HTTP_200_OK,
        )
