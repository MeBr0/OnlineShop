from django.urls import path

from .views import UserListView, UserCreateView
from .views import login, logout, me


urlpatterns = [
    path('', UserListView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('me/', me),

]