from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# manager class for model Order
class OrderManager(models.Manager):

    def for_user(self, user):
        return self.filter(owner=user)


class Order(models.Model):

    count = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} of {} for {}'.format(self.count, self.product, self.owner)
