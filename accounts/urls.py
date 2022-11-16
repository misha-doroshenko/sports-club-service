from django.urls import path

from accounts.views import login_view, sign_up_view, logout_view

urlpatterns = [
    path("accounts/login/", login_view, name="login"),
    path("accounts/sign-up/", sign_up_view, name="sign-up"),
    path("accounts/logout/", logout_view, name="logout"),
]

app_name = "accounts"
