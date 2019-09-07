from django.urls import path

from order.views import OrderListView, OrderView, create_orders

# prefix order/
urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderView.as_view()),
    path('many/', create_orders),
]
