from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name="name")

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="name")
    sugar = models.IntegerField(default=0)
    coffee = models.IntegerField(default=0)
    flour = models.IntegerField(default=0)
    chocolate = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name="products", verbose_name="categories", blank=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
