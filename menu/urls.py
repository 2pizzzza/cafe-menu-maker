from django.urls import path

from .views import CategoryListView, CategoryDetailView, MealsDetailView, CategoryWithMealsListView,  \
     ReviewListView, GalleryListView

urlpatterns = [
    # Category Endpoints
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Get all categories with all his meals
    path('categories-with-meals/', CategoryWithMealsListView.as_view(), name='categories-with-meals'),

    # Meals Endpoints
    path('meals/<int:pk>/', MealsDetailView.as_view(), name='meals-detail'),


    # Revies
    path("reviews/", ReviewListView.as_view(), name='review-list'),

    # Gallery
    path('galleries/', GalleryListView.as_view(), name='gallery'),
]
