from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=999)
    image_url = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{} (Category: {}, Count: {})'.format(self.name, self.category, self.count)

