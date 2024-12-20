from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersByDayView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        date_str = self.kwargs['date_str']
        date = parse_date(date_str)
        if date is None:
            return Order.objects.none()
        return Order.objects.filter(date=date)


class OrdersByWeekView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        date_str = self.kwargs['date_str']
        date = parse_date(date_str)
        if date is None:
            return Order.objects.none()
        week_start = date - timedelta(days=date.weekday())
        week_end = week_start + timedelta(days=6)
        return Order.objects.filter(date__range=[week_start, week_end])


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                self.perform_update(serializer)
                return Response(serializer.data)
            except ValidationError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FreeTablesView(APIView):
    def get(self, request, date_str):
        date = parse_date(date_str)
        if date is None:
            return Response({'error': 'Неверный формат даты'}, status=400)

        free_tables = Order.get_free_tables_on_date(date)
        return Response(free_tables)

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
