
from accident_detection_api.models.incidents import Incident
from accident_detection_api.serializers import IncidentSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class IncidentListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the incidents  for given requested user
        '''
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Log the incident
        '''
        data = {
            'longitude': request.data.get('longitude'), 
            'latitude': request.data.get('latitude'), 

        }
        serializer = IncidentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
