from django.urls import path
from product import views

urlpatterns = [
    path('', views.get_product),
]