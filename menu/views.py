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

import os
from django.conf import settings

def list_media_files():
    media_root = settings.MEDIA_ROOT
    try:
        files = os.listdir(media_root)
        print("Files in directory:", media_root)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory not found: {media_root}")
    except Exception as e:
        print(f"An error occurred: {e}")

list_media_files()
