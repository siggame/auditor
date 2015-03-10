from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import ServiceSerializer
from .models import Service


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)
