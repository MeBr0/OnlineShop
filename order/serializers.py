from django.shortcuts import get_object_or_404

from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers import ProductSerializer
from user.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):

    status = serializers.BooleanField(read_only=True)
    owner = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'count', 'product', 'product_id', 'status', 'owner', )

    def create(self, validated_data):
        # pop and search product by id
        product_id = validated_data.pop('product_id')
        product = get_object_or_404(Product, id=product_id)

        if product.count < validated_data.get('count'):
            validated_data.pop('count')
            order = Order.objects.create(product=product, count=-1, **validated_data)

        else:
            product.count -= validated_data.get('count')
            product.save()

            # create product with given product
            order = Order.objects.create(product=product, **validated_data)

        return order


# class OrderListSerializer(serializers.ModelSerializer):
#
#     orders = OrderSerializer(many=True)
#
#     class Meta:
#         model = Order
#         fields = ('orders', )
#
#     def create(self, validated_data):
#
#         orders = validated_data.pop('orders')
#
#         order_list = []
#
#         for order in orders:
#             print(order)
#             print(order.get('product_id'))
#             product = Product.objects.get(id=order.get('product_id'))
#
#             new_order = Order.objects.create(product=product, **order)
#
#             order_list.append(new_order)
#
#         return order_list

