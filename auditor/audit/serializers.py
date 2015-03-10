from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
