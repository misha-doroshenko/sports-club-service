from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from club.models import Sport, Trainer, SportsClub, Workout


class SportForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Provide description for this sport",
                "row": 6,
                "class": "form-control"
            }
        ))
    sport_avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control"
                }
        ))

    class Meta:
        model = Sport
        fields = (
            "name",
            "description",
            "sport_avatar",
        )


class TrainerCreateForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    sports_club = forms.ModelChoiceField(
        queryset=SportsClub.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Sports Club",
                "class": "form-select"
            }
        ))
    sport = forms.ModelChoiceField(
        queryset=Sport.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Sport",
                "class": "form-select"
            }
        ))
    experience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Years",
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    trainer_avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control file-selector-button"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    def clean_experience(self):
        if self.cleaned_data["experience"] < 0:
            raise ValidationError("Experience must be a positive number")
        return self.cleaned_data["experience"]

    class Meta:
        model = Trainer
        fields = (
            "first_name",
            "last_name",
            "sports_club",
            "experience",
            "username",
            "email",
            "trainer_avatar",
            "password1",
            "password2"
        )


class TrainerUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    sports_club = forms.ModelChoiceField(
        queryset=SportsClub.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Sports Club",
                "class": "form-select"
            }
        ))
    experience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Experience",
                "class": "form-control"
            }
        ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    trainer_avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control file-selector-button"
            }
        ))

    def clean_experience(self):
        if self.cleaned_data["experience"] < 0:
            raise ValidationError("Experience must be a positive number")
        return self.cleaned_data["experience"]

    class Meta:
        model = Trainer
        fields = (
            "first_name",
            "last_name",
            "sports_club",
            "experience",
            "username",
            "email",
            "trainer_avatar",
        )


class SportsClubForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "form-control"
            }
        ))
    swimming_pool = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input"
            }
        ))
    sports_club_avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "class": "form-control"
                }
        ))

    class Meta:
        model = SportsClub
        fields = (
            "name",
            "address",
            "city",
            "swimming_pool",
            "sports_club_avatar",
        )


class WorkoutForm(forms.ModelForm):
    sport = forms.ModelChoiceField(
        queryset=Sport.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Sport",
                "class": "form-select"
            }
        ))
    weekday = forms.ChoiceField(
        choices=Workout.WEEKDAY_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Weekday",
                "class": "form-select"
            }
        ))
    beginning_time = forms.ChoiceField(
        choices=Workout.HOUR_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Beginning time",
                "class": "form-select"
            }
        ))
    ending_time = forms.ChoiceField(
        choices=Workout.HOUR_CHOICES,
        widget=forms.Select(
            attrs={
                "placeholder": "Ending time",
                "class": "form-select"
            }
        ))

    def clean(self):
        if self.cleaned_data["ending_time"] <= self.cleaned_data["beginning_time"]:
            raise ValidationError("Beginning time must be earlier that ending time")
        return super(WorkoutForm, self).clean()

    class Meta:
        model = Workout
        fields = (
            "sport",
            "weekday",
            "beginning_time",
            "ending_time",
        )