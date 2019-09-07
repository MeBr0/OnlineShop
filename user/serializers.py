from django.contrib.auth.models import User

from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    # encoder used in project
    encoder = BCryptSHA256PasswordHasher()

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'groups', 'is_superuser', 'password', "first_name", "last_name", )

    def create(self, validated_data):
        # get and encode password
        password = validated_data.pop('password')
        hashed_password = self.encoder.encode(password, salt=self.encoder.salt())

        # get and assign groups
        groups = validated_data.pop('groups')
        user = User.objects.create(password=hashed_password, **validated_data)
        user.groups.set(groups)

        user.save()

        return user
