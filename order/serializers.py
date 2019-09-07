from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers import ProductOrderSerializer
from user.serializers import UserSerializer


# default serializer for generic view
class OrderSerializer(serializers.ModelSerializer):

    # status default value is False
    status = serializers.BooleanField(read_only=True)

    # owner get by OrderManager
    owner = UserSerializer(read_only=True)

    product = ProductOrderSerializer()

    class Meta:
        model = Order
        fields = ('id', 'count', 'product', 'status', 'owner', )

    def create(self, validated_data):

        # get product from database
        product = Product.objects.get(id=validated_data.pop('product')['id'])

        # check whether order's count is greater than product's count
        if product.count < validated_data.get('count'):
            validated_data.pop('count')

            # set count to -1, because their is not enough products
            order = Order.objects.create(count=-1, product=product, **validated_data)

        else:
            # decrease product's count by order's count
            product.count -= validated_data.get('count')
            product.save()

            order = Order.objects.create(product=product, **validated_data)

        return order
