import json

from django.contrib.auth.models import User, AnonymousUser
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from order.models import Order
from order.permissions import IsOwner, Rejected
from order.serializers import OrderSerializer


class OrderListView(generics.ListCreateAPIView):

    def get_queryset(self):
        if self.request.method == 'GET':
            # if user in group 1 (User) -> self objects
            if User.objects.filter(username=self.request.user.username, groups=(1, )):
                return Order.objects.for_user(self.request.user)

            # else -> all objects
            return Order.objects.all()

        elif self.request.method == 'POST':
            # can create only by user in group 1 (User)
            if User.objects.filter(username=self.request.user.username, groups=(1, )):
                return Order.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return OrderSerializer

    # bind order with user who send request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):

        if self.request.method == 'GET':
            return IsAuthenticated(),

        elif self.request.method == 'POST':
            # check user is in group 1 (User)
            if User.objects.filter(username=self.request.user.username, groups=(1, )):
                return IsAuthenticated(),

            return Rejected(),


class OrderView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        # can create only by user in group 1 (User)
        if User.objects.filter(username=self.request.user.username, groups=(1, )):
            return Order.objects.for_user(self.request.user)

        # else -> all objects
        return Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializer

    def get_permissions(self):

        if self.request.method == 'GET':
            # check user is in group 1 (User)
            if User.objects.filter(username=self.request.user.username, groups=(1, )):
                return IsAuthenticated(), IsOwner(),

            return AllowAny(),

        elif self.request.method == 'PUT':
            # check user is in group 1 (User)
            if User.objects.filter(username=self.request.user.username, groups=(1, )):
                return IsAuthenticated(), IsOwner(),

            # check user is in group 2 (Manager)
            elif User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),

        elif self.request.method == "DELETE":
            # check user is in group 2 (Manager)
            if User.objects.filter(username=self.request.user.username, groups=(2, )):
                return IsAuthenticated(),

            # admin rights
            return IsAdminUser(),


# create list of orders
@api_view(['POST'])
def create_orders(request):
    result_orders = []

    # check user authorized
    if isinstance(request.user, AnonymousUser):
        return Response({"detail": "Authentication credentials were not provided."},
                        status=status.HTTP_401_UNAUTHORIZED)

    # check user is in group 1 (User)
    if User.objects.filter(username=request.user.username, groups=(1, )):
        # get json orders
        orders = json.loads(request.body).get('orders')

        for order in orders:
            order_serializer = OrderSerializer(data=order)

            # check or raise exception
            order_serializer.is_valid(raise_exception=True)

            # if success -> create order and push to result
            order_serializer.save(owner=request.user)
            result_orders.append(order_serializer.data)

        data = {'orders': result_orders}
        return Response(data, status=status.HTTP_201_CREATED)

    return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)









