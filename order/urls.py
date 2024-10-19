from django.urls import path
from .views import OrderListCreateView, OrderRetrieveView, OrdersByDayView, OrdersByWeekView

urlpatterns = [
    # Create order and get all orders
    path('orders/', OrderListCreateView.as_view(), name='orders-list-create'),

    # Get order by id
    path('orders/<int:pk>/', OrderRetrieveView.as_view(), name='orders-retrieve'),

    # Get by day
    path('orders/by-day/<str:date_str>/', OrdersByDayView.as_view(), name='orders-by-day'),

    # Get by week
    path('orders/by-week/<str:date_str>/', OrdersByWeekView.as_view(), name='orders-by-week'),
]
