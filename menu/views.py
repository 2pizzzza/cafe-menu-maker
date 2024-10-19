from rest_framework import generics

from .models import Category, Meals, Review, Gallery
from .serializers import CategorySerializer, CategoryDetailSerializer, MealsSerializer, \
    ReviewSerializer, GallerySerializer


# Menu
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


# Review
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Gallery
class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
