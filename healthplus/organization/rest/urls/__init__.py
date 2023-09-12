from django.urls import path, include


urlpatterns = [
    path(r"user-login", include("organization.rest.urls.login")),
]