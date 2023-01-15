# todo/todo_api/serializers.py
from accident_detection_api.models.emergency_sites import EmergencySite
from accident_detection_api.models.incidents import Incident
from accident_detection_api.models.responders import Responder
from rest_framework import serializers


class EmergencySiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencySite
        fields = ["sid", "name", "longitude","latitude", "is_active", "address"]
        
        
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ["sid", "longitude","latitude", "is_valid"]
        
        
class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = ["sid", "first_name", "last_name", "longitude","latitude", "is_active"]