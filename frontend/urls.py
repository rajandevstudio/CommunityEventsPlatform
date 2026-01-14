from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page),
    path("register/", views.register_page),
    path("logout/", views.login_page),
    path("events/", views.events_page),
    path("events/create/", views.event_create_page),
    path("profile/", views.profile_page),
]
