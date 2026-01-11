from rest_framework.permissions import BasePermission

class IsOrganizer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "organizer"
        )

class IsEventOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
