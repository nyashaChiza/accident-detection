from accident_detection_api.views.emergency_site_views import \
    EmergencySiteListApiView
from accident_detection_api.views.incident_views import IncidentListApiView
from accident_detection_api.views.responder_views import ResponderListApiView
from django.urls import include, path

urlpatterns = [
    path('api/emergency-sites', EmergencySiteListApiView.as_view()),
    path('api/responders', ResponderListApiView.as_view()),
    path('api/incidents', IncidentListApiView.as_view()),
]
