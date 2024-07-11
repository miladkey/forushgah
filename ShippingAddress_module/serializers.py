from rest_framework import serializers
from Order_module.models import Order
from ShippingAddress_module.models import ShippingAddress


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order = ShippingAddressSerializer(read_only=True, many=True)   #_set
    class Meta:
        model = Order
        fields = '__all__'