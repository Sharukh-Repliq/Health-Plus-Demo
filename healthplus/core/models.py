from django.db import models
import uuid
from autoslug import AutoSlugField

class AbstractBaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, populate_from='name')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)
