from django.urls import path

from club.views import index, SportListView, SportDetailView, SportUpdateView, SportCreateView, SportDeleteView, \
    TrainerListView

urlpatterns = [
    path("", index, name="index"),
    path("sports/", SportListView.as_view(), name="sport-list"),
    path("sports/<int:pk>/", SportDetailView.as_view(), name="sport-detail"),
    path("sports/create", SportCreateView.as_view(), name="sport-create"),
    path("sports/<int:pk>/update", SportUpdateView.as_view(), name="sport-update"),
    path("sports/<int:pk>/delete", SportDeleteView.as_view(), name="sport-delete"),
    path("trainers/", TrainerListView.as_view(), name="trainers-list"),
]

app_name = "club"
