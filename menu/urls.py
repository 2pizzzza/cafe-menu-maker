from django.urls import path
from .views import CategoryListView, CategoryDetailView, MealsDetailView

urlpatterns = [
    # Category Endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Meals Endpoints
    path('meals/<int:pk>/', MealsDetailView.as_view(), name='meals-detail'),
]
