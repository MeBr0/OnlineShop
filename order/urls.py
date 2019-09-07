from django.urls import path

from order.views import create_orders
from .views import OrderListView, OrderView


urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderView.as_view()),
    path('many/', create_orders),
]
