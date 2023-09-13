from django.shortcuts import get_object_or_404

from rest_framework import generics

from organization.models import OrganizationUser
from ..serializers.doctor import DoctorSerializer
from organization.rest.permissions import IsOrganizationMember


class DoctorList(generics.ListCreateAPIView):
    ''' Create or view list for all the organization doctors for ogranization users'''
    permission_classes = [IsOrganizationMember]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        user = self.request.user
        organization = user.OrganizationUser_set.first().organization
        return self.queryset.filter(organization)


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    ''' Retrive, update or delete organization doctors for ogranization users'''
    permission_classes = [IsOrganizationMember]
    serializer_class = DoctorSerializer
    lookup_field = 'uid'

