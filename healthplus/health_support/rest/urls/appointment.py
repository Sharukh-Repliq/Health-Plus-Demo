from django.urls import path

from ..views.appointment import CreateAppointmentWithDoctorView


urlpatterns = [
    path(
        r"appointment/doctors/<uuid:uid>",
        CreateAppointmentWithDoctorView.as_view(),
        name="create-appointment-with-doctor",
    ),
]

# path(
#     r"/we/doctors/<uuid:uid>",
#     DoctorDetail.as_view(),
#     name="doctor-detail",
# )
