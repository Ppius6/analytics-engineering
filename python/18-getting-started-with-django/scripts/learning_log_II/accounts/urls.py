"""Defines URL patterns for user accounts."""

from django.urls import path, include

app_name = "accounts"
urlpatterns = [
    # Include default auth urls (login, logout, password management)
    path("", include("django.contrib.auth.urls")),
]
