from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


@api_view(['POST'])
def login(request):
    # check whether user data is valid, or raise exception
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # get user from DB
    user = serializer.validated_data['user']

    # creates token if exists, or return existing
    token, created = Token.objects.get_or_create(user=user)

    data = { 'token': token.key }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request):
    # delete token
    request.auth.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
