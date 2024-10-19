from decimal import Decimal

from django.core import validators
from django.db import models


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
                                validators=[validators.MinValueValidator(Decimal('0.0'))])
    picture = models.ImageField("Image", null=True, blank=True, upload_to="images/")
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'


class Review(models.Model):
    """Review Model"""

    picture = models.ImageField("Image", upload_to="images/")

    def __str__(self):
        return str(self.picture)


class Gallery(models.Model):
    """Galleries Model"""

    picture = models.ImageField("Image", upload_to="images/")

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return str(self.picture)
