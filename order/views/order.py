import json

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer


class OrderListView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializer

    # bind order with user who send request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializer


# create list of orders in single request
@api_view(['POST'])
def create_orders(request):
    result_orders = []

    # get json orders
    orders = json.loads(request.body).get('orders')

    for order in orders:
        order_serializer = OrderSerializer(data=order)

        # check or raise exception
        order_serializer.is_valid(raise_exception=True)

        # if success -> create order and push to result
        order_serializer.save(owner=request.user)
        result_orders.append(order_serializer.data)

    data = { 'orders': result_orders }
    return Response(data, status=status.HTTP_201_CREATED)





