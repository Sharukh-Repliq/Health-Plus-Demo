from django.urls import path

from ..views.login import UserLoginView


urlpatterns = [
    path(
        r"",
        UserLoginView.as_view(),
        name="user-login",
    ),
]