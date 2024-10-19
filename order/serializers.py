from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'email', 'phone', 'date', 'start_order', 'end_order', 'total_guests', 'comment']
