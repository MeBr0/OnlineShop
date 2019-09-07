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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializer


@api_view(['POST'])
def create_orders(request):
    orders = json.loads(request.body).get('orders')
    order_list = []

    for order in orders:
        order_serializer = OrderSerializer(data=order)

        if order_serializer.is_valid():
            order_serializer.save(owner=request.user)

            order_list.append(order_serializer.data)

    return Response({'orders': order_list}, status=status.HTTP_201_CREATED)





