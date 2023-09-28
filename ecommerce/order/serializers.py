from rest_framework import serializers
from decimal import Decimal, ROUND_DOWN
from product.serializers import ProductSerializer
from .models import Order, OrderItem

class MyOrderItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "cap",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )

class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, rounding=ROUND_DOWN)

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "cap",
            "place",
            "phone",
            "stripe_token",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order