from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url='login/', permanent=False)),
    path("login/", views.login_page),
    path("register/", views.register_page),
    path("logout/", views.login_page),
    path("events/", views.events_page),
    path("events/create/", views.event_create_page),
    path("profile/", views.profile_page),
]
