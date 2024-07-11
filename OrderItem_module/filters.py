import django_filters
from OrderItem_module.models import OrderItem


class OrderItemFilter(django_filters.FilterSet):

    class Meta:
         model = OrderItem
         exclude = ['image']

