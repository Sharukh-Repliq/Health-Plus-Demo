
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # organization app
    path("api/", include("organization.rest.urls"))
]
