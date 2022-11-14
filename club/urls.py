from django.urls import path

from club.views import index, SportListView, SportDetailView, SportUpdateView, SportCreateView, SportDeleteView, \
    TrainerListView, TrainerDetailView, TrainerUpdateView, TrainerCreateView, TrainerDeleteView, SportsClubListView, \
    SportsClubDetailView, SportsClubCreateView, SportsClubUpdateView, SportsClubDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("sports/", SportListView.as_view(), name="sport-list"),
    path("sports/<int:pk>/", SportDetailView.as_view(), name="sport-detail"),
    path("sports/create", SportCreateView.as_view(), name="sport-create"),
    path("sports/<int:pk>/update", SportUpdateView.as_view(), name="sport-update"),
    path("sports/<int:pk>/delete", SportDeleteView.as_view(), name="sport-delete"),
    path("trainers/", TrainerListView.as_view(), name="trainer-list"),
    path("trainers/<int:pk>/", TrainerDetailView.as_view(), name="trainer-detail"),
    path("trainers/sign-up", TrainerCreateView.as_view(), name="sign-up"),
    path("trainers/<int:pk>/update", TrainerUpdateView.as_view(), name="trainer-update"),
    path("trainers/<int:pk>/delete", TrainerDeleteView.as_view(), name="trainer-delete"),
    path("sports-clubs/", SportsClubListView.as_view(), name="sports-club-list"),
    path("sports-clubs/<int:pk>/", SportsClubDetailView.as_view(), name="sports-club-detail"),
    path("sports-clubs/create", SportsClubCreateView.as_view(), name="sports-club-create"),
    path("sports-clubs/<int:pk>/update", SportsClubUpdateView.as_view(), name="sports-club-update"),
    path("sports-clubs/<int:pk>/delete", SportsClubDeleteView.as_view(), name="sports-club-delete"),
]

app_name = "club"
