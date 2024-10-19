from django.shortcuts import render
from rest_framework import generics

from event.serializers import EventDetailSerializer
from event import models as m


# Events
class EventListView(generics.ListAPIView):
    queryset = m.Event.objects.all()
    serializer_class = EventDetailSerializer


class EventDetailView(generics.RetrieveAPIView):
    queryset = m.Event.objects.all()
    serializer_class = EventDetailSerializer
