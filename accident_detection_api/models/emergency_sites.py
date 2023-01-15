import uuid

from django.db import models


class EmergencySite(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
