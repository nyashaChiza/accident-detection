
from accident_detection_api.models.responders import Responder
from accident_detection_api.serializers import ResponderSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class ResponderListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the responders
        '''
        responders = Responder.objects.all()
        serializer = ResponderSerializer(responders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        add a new responder
        '''
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'longitude': request.data.get('longitude'), 
            'latitude': request.data.get('latitude'), 
        }
        serializer = ResponderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
