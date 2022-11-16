from unittest import TestCase

from club.forms import SportsClubForm, SportForm


class FormsTest(TestCase):
    def test_sports_club_form(self):
        form_data = {
            "name": "test123",
            "address": "test_street",
            "city": "test_city",
            "swimming_pool": True,
            "sports_club_avatar": None,
        }
        print(form_data)
        form = SportsClubForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_sport_form(self):
        form_data = {
            "name": "test_sport",
            "description": "",
            "sport_avatar": None,
        }
        print(form_data)
        form = SportForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
