from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from product.models import Product
from product.serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk'])

    def get_serializer_class(self):
        return ProductSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return AllowAny(),

        elif self.request.method == 'POST':
            # check user is in group 2 (Manager)
            if User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),


class ProductView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'], category=self.kwargs['pk2'])

    def get_serializer_class(self):
        return ProductSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return AllowAny(),

        elif self.request.method in ('PUT', "DELETE",):
            # check user is in group 2 (Manager)
            if User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),
