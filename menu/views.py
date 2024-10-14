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
from django.http import JsonResponse
from django.conf import settings


def list_files(request):
    media_root = settings.MEDIA_ROOT
    files = []
    try:
        for file in os.listdir(media_root):
            if file != 'venv':
                files.append(file)
    except FileNotFoundError:
        return JsonResponse({'error': 'Directory not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'files': files})


def list_project_files(request):
    base_dir = settings.BASE_DIR
    files_and_dirs = []

    for root, dirs, files in os.walk(base_dir):
        # Exclude the 'venv' directory
        if 'venv' in dirs:
            dirs.remove('venv')

        for name in files:
            files_and_dirs.append(os.path.relpath(os.path.join(root, name), base_dir))

        for name in dirs:
            files_and_dirs.append(os.path.relpath(os.path.join(root, name), base_dir))

    return JsonResponse({'files_and_dirs': files_and_dirs})
