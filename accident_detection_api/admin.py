from accident_detection_api.models.emergency_sites import EmergencySite
from accident_detection_api.models.incidents import Incident
from accident_detection_api.models.responders import Responder
from django.contrib import admin


# Register your models here.

admin.site.register(EmergencySite)

admin.site.register(Responder)

admin.site.register(Incident)


