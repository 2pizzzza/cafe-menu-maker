from django.urls import path
from .views import CategoryListView, CategoryDetailView, MealsDetailView, CategoryWithMealsListView, list_media_files

urlpatterns = [
    # Category Endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('show/', list_media_files)
    # Get all categories with all his meals
    path('categories-with-meals/', CategoryWithMealsListView.as_view(), name='categories-with-meals'),

    # Meals Endpoints
    path('meals/<int:pk>/', MealsDetailView.as_view(), name='meals-detail'),
]
