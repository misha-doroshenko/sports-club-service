from django.urls import path

from club.views import index, SportListView, SportDetailView, SportUpdateView, SportCreateView, SportDeleteView, \
    TrainerListView, TrainerDetailView, TrainerUpdateView, TrainerCreateView, TrainerDeleteView, SportsClubListView, \
    SportsClubDetailView, SportsClubCreateView, SportsClubUpdateView, SportsClubDeleteView, WorkoutListView, \
    toggle_assign_to_workout, WorkoutUpdateView, WorkoutCreateView, workout_delete

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
    path("workouts/", WorkoutListView.as_view(), name="workout-list"),
    path("workouts/<int:pk>/toggle-assign/", toggle_assign_to_workout, name="toggle-workout-assign"),
    path("workouts/<int:pk>/update", WorkoutUpdateView.as_view(), name="workout-update"),
    path("workouts/create", WorkoutCreateView.as_view(), name="workout-create"),
    path("workouts/<int:pk>/delete", workout_delete, name="workout-delete"),
]

app_name = "club"
