from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import Roomserializer
from studybud.base.api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializers = Roomserializer(rooms, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getRooms(request, pk):
    room = Room.objects.get(id=pk)
    serializers = Roomserializer(room, many=False) 
    return Response(serializers.data)
