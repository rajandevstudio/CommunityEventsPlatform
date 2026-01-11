from django.urls import path, include
from apis.auth.view import LoginView, RefreshTokenView
from rest_framework.routers import SimpleRouter
from apis.users.views import RegisterUserView, UserViewSet

router = SimpleRouter()
router.register(r'v1/users', UserViewSet, basename='users_v1')

urlpatterns = [
    # User registration (PUBLIC)
    path('v1/users/register/', RegisterUserView.as_view(), name='users_register_v1'),

    # User profile APIs (PROTECTED)
    path('', include(router.urls)),

    path('v1/web-auth/', LoginView.as_view(), name='get_token'),
    path('v1/web-auth/refresh/', RefreshTokenView.as_view(), name='refresh_token'),

]
