from rest_framework import serializers
from health_support.models import Appointment
from organization.models import Organization, Doctor
from organization.rest.serializers.we import OrganizationSerializer


class CreateAppointmentWithDoctorSerializer(serializers.Serializer):
    """Patient can create an Appointment for lab test or doctor"""

    uid = serializers.CharField()
    slug = serializers.CharField()
    patient = serializers.UUIDField()
    doctor = serializers.UUIDField()
    organization = OrganizationSerializer()
    schedule_start = serializers.DateTimeField()
    schedule_end = serializers.DateTimeField()
    location = serializers.CharField()
    type = serializers.CharField()
    status = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        doctor_uid = self.context["request"].query_params.get("doctor_uid")

        # Fetch the Doctor and Patient instances based on the UID
        try:
            doctor = Doctor.objects.get(uid=doctor_uid)

        except Doctor.DoesNotExist:
            raise serializers.ValidationError(
                "Doctor with the specified UID does not exist."
            )

        # Create the Appointment object with doctor, patient, and validated data
        appointment = Appointment.objects.create(
            doctor=doctor, patient=user, **validated_data
        )

        return appointment


class CreateAppointmentForLabTestSerializer(serializers.Serializer):
    """Patient can create an appointment for lab test"""

    pass
