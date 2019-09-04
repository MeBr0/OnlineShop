from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from user.serializers import UserSerializer


# register new user
class UserCreateView(generics.CreateAPIView):

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer


# get list of all users (admin ONLY)
class UserListView(generics.ListAPIView):

    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
