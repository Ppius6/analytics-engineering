"""Defines URL patterns for user accounts."""

from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    # Include default auth urls (login, logout, password management)
    path("", include("django.contrib.auth.urls")),
    # Registration page
    path("register/", views.register, name="register"),
]
