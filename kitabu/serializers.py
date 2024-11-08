from rest_framework import serializers
from .models import Customer, Order


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'code']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='customer',
        queryset=Customer.objects.all()
    )

    class Meta:
        model = Order
        fields = ['id', 'item', 'price', 'time', 'customer', 'customer_id']
