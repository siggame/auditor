from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Meeting, Attendance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'email',)


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ('name', 'date', 'created', 'head_count', 'present')


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
