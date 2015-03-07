from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, MeetingSerializer, AttendanceSerializer
from .models import Meeting


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MeetingList(generics.ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = (AllowAny,)


class AttendanceCreate(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = (AllowAny,)
