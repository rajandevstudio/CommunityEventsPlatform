from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

class LoginView(TokenObtainPairView):

    @extend_schema(
        tags=["Auth"],
        summary="Login (username & password)",
        description=(
            "Authenticate using username and password.\n\n"
            "Returns **access** and **refresh** JWT tokens."
        ),
        request=TokenObtainPairSerializer,
        responses={
            200: TokenObtainPairSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




class RefreshTokenView(TokenRefreshView):

    @extend_schema(
        tags=["Auth"],
        summary="Refresh access token",
        description="Generate a new access token using a refresh token",
        request=TokenRefreshSerializer,
        responses={200: TokenRefreshSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
