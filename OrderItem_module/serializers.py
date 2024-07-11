from rest_framework import serializers
from OrderItem_module.models import OrderItem
from Order_module.models import Order
from Product_module.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = '__all__'







































# from rest_framework import serializers
# from OrderItem_module.models import OrderItem
# from Order_module.serializers import OrderSerializer
# from Product_module.serializers import ProductSerializer
#
#
# class OrderItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True, many=True)
#     order = OrderSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = OrderItem
#         fields = '__all__'
#
#
