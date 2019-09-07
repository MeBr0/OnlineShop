from django.urls import path

from user.views import UserView, login, logout, me


urlpatterns = [
    path('', UserView.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('me/', me),

]
