# Events
from rest_framework import serializers

from event.models import ImageForEvent, Event


class ImageForEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageForEvent
        fields = ['id', 'picture', 'is_main']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date']


class EventDetailSerializer(serializers.ModelSerializer):
    pictures = ImageForEventSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'pictures']

