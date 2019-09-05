from rest_framework import generics

from product.models import Category
from product.serializers import CategorySerializer


class CategoryListView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer


class CategoryView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer
