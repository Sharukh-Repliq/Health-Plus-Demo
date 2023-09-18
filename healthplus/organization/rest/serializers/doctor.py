from rest_framework import serializers
from organization.models import Doctor
from .user import UserSerializer
from organization.helper.user import UserService

from phonenumber_field.serializerfields import PhoneNumberField


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "user",
            "designation",
            "specialty",
            "expertise",
        ]


class DoctorSerializer(serializers.Serializer):
    uid = serializers.ReadOnlyField()
    slug = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    user = UserSerializer()
    designation = serializers.CharField(max_length=255)
    specialty = serializers.CharField(max_length=50)
    expertise = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """Create an User then assign that user as a Patient"""
        user_helper = UserService()

        # Create User
        user = user_helper.create_user(
            phone=validated_data.get("phone"),
            password=validated_data.get("password", str(validated_data["phone"])),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            email=validated_data.get("email", ""),
        )

        # Set that user as an patient
        patient = Patient.objects.create(user=user.id)

        return validated_data
