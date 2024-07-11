from django.contrib.auth.models import User
from rest_framework import serializers
from Product_module.models import Product




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user = ProductSerializer(read_only=True, many=True)   #_set
    class Meta:
        model = User
        fields = '__all__'