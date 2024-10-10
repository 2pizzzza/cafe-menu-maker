from django.core import validators
from django.db import models

from main import settings


class Category(models.Model):
    """Category Model"""

    name = models.CharField('Name category', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Meals(models.Model):
    """Meals Model"""

    name = models.CharField("Name", max_length=30, db_index=True, unique=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2, default=100,
                                validators=[validators.MinValueValidator(0)])
    picture = models.ImageField("Image", null=True, blank=True, upload_to=settings.MENU_IMAGE_FOLDER)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'