import django_filters
from ShippingAddress_module.models import ShippingAddress


class ShippingAddressFilter(django_filters.FilterSet):

    class Meta:
         model = ShippingAddress
         fields = '__all__'

