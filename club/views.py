from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from club.forms import SportForm, TrainerCreateForm, TrainerUpdateForm
from club.models import Trainer, SportsClub, Sport


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
    paginate_by = 8


class SportDetailView(generic.DetailView):
    model = Sport
    queryset = Sport.objects.all().prefetch_related("trainers", "workouts")


class SportCreateView(generic.CreateView):
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy("club:sport-list")


class SportUpdateView(generic.UpdateView):
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy("club:sport-list")


class SportDeleteView(generic.DeleteView):
    model = Sport
    success_url = reverse_lazy("club:sport-list")


class TrainerListView(generic.ListView):
    model = Trainer
    queryset = Trainer.objects.select_related("sport")
    paginate_by = 8


class TrainerDetailView(generic.DetailView):
    model = Trainer
    queryset = Trainer.objects.select_related("sport", "sports_club")


class TrainerCreateView(generic.CreateView):
    model = Trainer
    form_class = TrainerCreateForm
    template_name = "accounts/sign_up.html"
    success_url = reverse_lazy("club:trainer-list")


class TrainerUpdateView(generic.UpdateView):
    model = Trainer
    form_class = TrainerUpdateForm
    template_name = "club/trainer_update_form.html"
    success_url = reverse_lazy("club:trainer-list")


class TrainerDeleteView(generic.DeleteView):
    model = Trainer
    success_url = reverse_lazy("club:trainer-list")

