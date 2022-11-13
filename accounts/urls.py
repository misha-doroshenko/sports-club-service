from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import login_view, sign_up_view, logout_view

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', sign_up_view, name="sign-up"),
    path("logout/", logout_view, name="logout"),
]

app_name = "accounts"
