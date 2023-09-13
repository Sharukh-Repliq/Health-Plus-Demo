from rest_framework import serializers
from organization.models import Doctor
from .user import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['uid', 'slug', 'created_at', 'updated_at', 'user', 'designation', 'specialty', 'expertise']