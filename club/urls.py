from django.urls import path

from club.views import index, SportListView, SportDetailView

urlpatterns = [
    path("", index, name="index"),
    path("sports/", SportListView.as_view(), name="sport-list"),
    path("sports/<int:pk>", SportDetailView.as_view(), name="sport-detail"),
]

app_name = "club"
