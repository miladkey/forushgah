from django.contrib.auth.models import User
from rest_framework import serializers
from Product_module.models import Product
from Review_module.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product = ReviewSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user = ReviewSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'



