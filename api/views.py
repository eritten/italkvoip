from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Server
from .serializers import ServerSerializer


# Create your views here.
@api_view(['GET'])
def get_servers(request):
    servers = Server.objects.all()
    serializer = ServerSerializer(servers, many=True)
    return Response(serializer.data)
