from rest_framework import serializers
from .models import Customer, Product, Order, OrderLine

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['__all__']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Order
        fields = ['__all__']

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields= ['__all__']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']

