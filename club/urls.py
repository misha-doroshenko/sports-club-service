from django.urls import path

from club.views import index, SportListView

urlpatterns = [
    path("", index, name="index"),
    path("sports/", SportListView.as_view(), name="sport-list"),
]

app_name = "club"
