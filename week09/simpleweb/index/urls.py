from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index),
    path('login', views.login_page, name='login'),
    path('logined', views.logined_page),
    path("logout", auth_view.LogoutView.as_view(
        next_page="login"), name="logout"),
]
