from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.serializers import UserSerializer


@api_view(['GET'])
def me(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        exception = {"detail": "Authentication credentials were not provided."}

        return Response(exception, status=status.HTTP_401_UNAUTHORIZED)
