import django_filters
from Product_module.models import Product


class ProductFilter(django_filters.FilterSet):

    class Meta:
         model = Product
         exclude = ['image']

