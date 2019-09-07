from django.contrib.auth.models import User

from rest_framework import generics

from user.serializers import UserSerializer


class UserView(generics.ListCreateAPIView):

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
