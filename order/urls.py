from django.urls import path

# from order.views import OrdersView
from .views import OrderListView, OrderView


urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:pk>/', OrderView.as_view()),
    # path('many/', OrdersView.as_view()),
]
