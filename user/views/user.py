from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from user.serializers import UserSerializer


class UserView(generics.ListCreateAPIView):

    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            # check user is in group 2 (Manager)
            if User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),

        elif self.request.method == 'POST':
            return AllowAny(),
