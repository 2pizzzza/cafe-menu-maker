from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import OrderListCreateView, OrderRetrieveView, OrdersByDayView, OrdersByWeekView, OrderUpdateView, \
    OrderDeleteView

urlpatterns = [
    # Create order and get all orders
    path('orders/', OrderListCreateView.as_view(), name='orders-list-create'),

    # Get order by id
    path('orders/<int:pk>/', OrderRetrieveView.as_view(), name='orders-retrieve'),

    # Update order
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='orders-update'),

    # Delete order
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='orders-delete'),

    # Get by day
    path('orders/by-day/<str:date_str>/', OrdersByDayView.as_view(), name='orders-by-day'),

    # Get by week
    path('orders/by-week/<str:date_str>/', OrdersByWeekView.as_view(), name='orders-by-week'),

    # Login for Admin
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
