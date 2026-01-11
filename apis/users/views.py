from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from users.models import User
from apis.users.serializers import UserSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from drf_spectacular.utils import OpenApiResponse
@extend_schema(
    tags=["Auth"],
    summary="Register a new user",
    description=(
        "Create a new user account.\n\n"
        "**Required fields:**\n"
        "- username\n"
        "- password\n"
        "- role"
    ),
    request=UserSerializer,
    responses={
        201: UserSerializer,
        400: OpenApiResponse(description="Validation error"),
    },
)
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]





@extend_schema_view(
    list=extend_schema(
        tags=["Users"],
        summary="Get logged-in user details",
        description="Returns details of the currently authenticated user",
        responses={200: UserSerializer(many=True)},
    ),
    retrieve=extend_schema(
        tags=["Users"],
        summary="Retrieve user",
        description="Retrieve user details (self only)",
        responses={200: UserSerializer},
    ),
)
class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

