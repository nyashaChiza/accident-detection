from accident_detection_api.models.emergency_sites import EmergencySite
from accident_detection_api.serializers import EmergencySiteSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class EmergencySiteListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Emergency Sites
        '''
        responders = EmergencySite.objects.all()
        serializer = EmergencySiteSerializer(responders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        add a new Emergency Site
        '''
        data = {
            'name': request.data.get('name'),
            'longitude': request.data.get('longitude'), 
            'latitude': request.data.get('latitude'), 
            'address': request.data.get('address'), 

        }
        serializer = EmergencySiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
