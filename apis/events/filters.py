import django_filters
from events.models import Event

class EventFilter(django_filters.FilterSet):
    start_after = django_filters.DateTimeFilter(
        field_name="start_time", lookup_expr="gte"
    )
    start_before = django_filters.DateTimeFilter(
        field_name="start_time", lookup_expr="lte"
    )

    location = django_filters.CharFilter(
        field_name="location", lookup_expr="icontains"
    )

    organizer = django_filters.NumberFilter(
        field_name="organizer__id"
    )

    class Meta:
        model = Event
        fields = ["location", "organizer"]
