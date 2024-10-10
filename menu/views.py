from rest_framework import generics
from .models import Category, Meals
from .serializers import CategorySerializer, CategoryDetailSerializer, MealsSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryWithMealsListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class MealsDetailView(generics.RetrieveAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
