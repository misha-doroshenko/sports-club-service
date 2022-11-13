from django.urls import path

from club.views import index, SportListView, SportDetailView, SportUpdateView, SportCreateView, SportDeleteView, \
    TrainerListView, TrainerDetailView, TrainerUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("sports/", SportListView.as_view(), name="sport-list"),
    path("sports/<int:pk>/", SportDetailView.as_view(), name="sport-detail"),
    path("sports/create", SportCreateView.as_view(), name="sport-create"),
    path("sports/<int:pk>/update", SportUpdateView.as_view(), name="sport-update"),
    path("sports/<int:pk>/delete", SportDeleteView.as_view(), name="sport-delete"),
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    path("trainers/<int:pk>/", TrainerDetailView.as_view(), name="trainer-detail"),
    path("trainers/<int:pk>/update", TrainerUpdateView.as_view(), name="trainer-update"),
]

app_name = "club"
