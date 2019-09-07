from django.urls import path

from product.views import CategoryListView, CategoryView, ProductListView, ProductView

# prefix category/
urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>/', CategoryView.as_view()),
    path('<int:pk>/product/', ProductListView.as_view()),
    path('<int:pk2>/product/<int:pk>/', ProductView.as_view()),

]
