import uuid

from django.db import models


class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)
    is_valid = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    response_time_in_minutes = models.IntegerField(null=True, blank=True,)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    