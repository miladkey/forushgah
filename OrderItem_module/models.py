from django.db import models

from Order_module.models import Order
from Product_module.models import Product


# Create your models here.

class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='order')
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='OrderItem', null=True, blank=True)

    def __str__(self):
        return self.name