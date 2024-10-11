from django.urls import path
from .views import CategoryListView, CategoryDetailView, MealsDetailView, CategoryWithMealsListView, list_files ,list_project_files

urlpatterns = [
    # Category Endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('list-project-files/', list_project_files, name='list-project-files'),
    path('list-files/', list_files, name='list-files'),
    # Get all categories with all his meals
    path('categories-with-meals/', CategoryWithMealsListView.as_view(), name='categories-with-meals'),

    # Meals Endpoints
    path('meals/<int:pk>/', MealsDetailView.as_view(), name='meals-detail'),
]
