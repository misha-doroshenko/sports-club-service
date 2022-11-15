from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from club.forms import SportForm, TrainerCreateForm, TrainerUpdateForm, SportsClubForm, WorkoutForm, SportSearchForm, \
    TrainerSearchForm, SportsClubSearchForm, WorkoutSearchForm
from club.models import Trainer, SportsClub, Sport, Workout


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
    queryset = Sport.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        name = self.request.GET.get("name", "")

        context = super(SportListView, self).get_context_data(**kwargs)
        context["search_form"] = SportSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = SportSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


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

    def get_context_data(self, *, object_list=None, **kwargs):
        name = self.request.GET.get("name", "")

        context = super(TrainerListView, self).get_context_data(**kwargs)
        context["search_form"] = TrainerSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = TrainerSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                first_name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


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


class SportsClubListView(generic.ListView):
    model = SportsClub
    template_name = "club/sports_club_list.html"
    context_object_name = "sports_club_list"
    paginate_by = 8
    queryset = SportsClub.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        name = self.request.GET.get("name", "")

        context = super(SportsClubListView, self).get_context_data(**kwargs)
        context["search_form"] = SportsClubSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = SportsClubSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class SportsClubDetailView(generic.DetailView):
    model = SportsClub
    queryset = SportsClub.objects.all().prefetch_related("trainers")
    template_name = "club/sports_club_detail.html"
    context_object_name = "sports_club"


class SportsClubCreateView(generic.CreateView):
    model = SportsClub
    form_class = SportsClubForm
    template_name = "club/sports_club_form.html"
    success_url = reverse_lazy("club:sports-club-list")


class SportsClubUpdateView(generic.UpdateView):
    model = SportsClub
    form_class = SportsClubForm
    template_name = "club/sports_club_form.html"
    success_url = reverse_lazy("club:sports-club-list")


class SportsClubDeleteView(generic.DeleteView):
    model = SportsClub
    template_name = "club/sports_club_confirm_delete.html"
    context_object_name = "sports_club"
    success_url = reverse_lazy("club:sports-club-list")


class WorkoutListView(generic.ListView):
    model = Workout
    paginate_by = 4
    queryset = Workout.objects.select_related("sport")

    def get_context_data(self, *, object_list=None, **kwargs):
        name = self.request.GET.get("name", "")

        context = super(WorkoutListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkoutSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = WorkoutSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                sport__name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class WorkoutUpdateView(generic.UpdateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("club:workout-list")


class WorkoutCreateView(generic.CreateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("club:workout-list")


def workout_delete(request, pk):
    Workout.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse_lazy("club:workout-list"))


@login_required
def toggle_assign_to_workout(request, pk):
    trainer = Trainer.objects.get(id=request.user.id)
    if (
        Workout.objects.get(id=pk) in trainer.workouts.all()
    ):
        trainer.workouts.remove(pk)
    else:
        trainer.workouts.add(pk)
    return HttpResponseRedirect(reverse_lazy("club:workout-list"))
