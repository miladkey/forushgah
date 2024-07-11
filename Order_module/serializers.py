from django.contrib.auth.models import User
from rest_framework import serializers
from Order_module.models import Order




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user = OrderSerializer(read_only=True, many=True)   #_set
    class Meta:
        model = User
        fields = '__all__'