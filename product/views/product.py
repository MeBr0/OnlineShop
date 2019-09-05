from rest_framework import generics

from product.models import Product
from product.serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk'])

    def get_serializer_class(self):
        return ProductSerializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'], category=self.kwargs['pk2'])

    def get_serializer_class(self):
        return ProductSerializer
