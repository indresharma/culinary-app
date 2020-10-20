from django.db import models
from django.contrib.auth import get_user_model

from products.models import BaseTracker

User = get_user_model()


class OrderItem(BaseTracker):
    item = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_item')
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.product}'

    def total_item_price(self):
        return self.quantity * self.item.price

class Order(BaseTracker):
    item = models.ManyToManyField('OrderItem')
    ordered = models.BooleanField(default=False)
    total_order_value = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total=0
        for order_item in self.item.all():
            total+= order_item.total_item_price()
        return total

    # def discounted_price(self):
    #     return self.total_price()*(100-self.coupon.discount)/100
        