from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


@api_view(['POST'])
def login(request):
    # checks whether user data is valid
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # gets info about user
    user = serializer.validated_data['user']

    # creates token if exists, or return existing
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    # deletes token
    # print(---request)

    request.auth.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
