from rest_framework import serializers
from .models import Category, Meals, Review, Gallery


# Menu
class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ['id', 'name', 'price', 'picture', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    meals = MealsSerializer(many=True, read_only=True, source='meals_set')

    class Meta:
        model = Category
        fields = ['id', 'name', 'meals']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'picture']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'picture']
