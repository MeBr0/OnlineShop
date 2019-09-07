from django.urls import path

from user.views import UserListView, UserCreateView, login, logout, me


urlpatterns = [
    path('', UserListView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('me/', me),

]
