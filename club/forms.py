from django import forms
from django.core.exceptions import ValidationError

from club.models import Sport, Trainer, SportsClub


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
