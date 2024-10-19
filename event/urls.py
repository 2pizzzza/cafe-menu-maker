from django.urls import path

from event.views import EventListView, EventDetailView

urlpatterns = [
    # Events
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),

]