from django.db import models


class OrganizationUserRoles(models.TextChoices):
    OWNER = "OWNER", "Owner"
    ADMIN = "owner", "Owner"
    MANAGER = "admin", "Admin"
    STAFF = "staff", "Staff"
