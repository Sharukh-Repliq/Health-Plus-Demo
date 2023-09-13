from django.urls import path, include


urlpatterns = [
    path(r"", include("organization.rest.urls.login")),
    path(r"", include("organization.rest.urls.doctor")),
]