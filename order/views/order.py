from rest_framework import generics

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


# class OrdersView(generics.CreateAPIView):
#
#     def get_queryset(self):
#         return Order.objects.all()
#
#     def get_serializer_class(self):
#         return OrderListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


