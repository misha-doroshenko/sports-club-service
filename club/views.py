from django.shortcuts import render
from django.views import generic

from club.models import Trainer, Workout, SportsClub, Sport


def index(request):
    """View function for the home page of the site."""

    num_trainers = Trainer.objects.count()
    num_sports_clubs = SportsClub.objects.count()
    num_sports = Sport.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_trainers": num_trainers,
        "num_sports_clubs": num_sports_clubs,
        "num_sports": num_sports,
        "num_visits": num_visits + 1,
    }

    return render(request, "club/index.html", context=context)


class SportListView(generic.ListView):
    model = Sport
