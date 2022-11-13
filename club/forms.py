from django import forms

from club.models import Sport


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
        fields = ('name', 'description', 'sport_avatar',)
