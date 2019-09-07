from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from product.models import Category
from product.serializers import CategorySerializer


class CategoryListView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return AllowAny(),

        elif self.request.method == 'POST':
            # check user is in group 2 (Manager)
            if User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),


class CategoryView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            return AllowAny(),

        elif self.request.method in ('PUT', "DELETE", ):
            # check user is in group 2 (Manager)
            if User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),
