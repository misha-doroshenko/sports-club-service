from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from club.models import Sport, SportsClub, Trainer

TRAINER_URL = reverse("club:trainer-list")
SPORTS_CLUB_URL = reverse("club:sports-club-list")
SPORT_URL = reverse("club:sport-list")
HOME = reverse("club:index")
LOGIN = reverse("accounts:login")


class PublicAccessForbiddenTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_public_access_forbidden_trainer(self):
        response = self.client.get(TRAINER_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_public_access_forbidden_sports_club(self):
        response = self.client.get(SPORTS_CLUB_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_public_access_forbidden_sport(self):
        response = self.client.get(SPORT_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_public_access_granted_login(self):
        response = self.client.get(LOGIN)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")


class PrivateAccessGrantedTest(TestCase):
    def setUp(self) -> None:
        sport = Sport.objects.create(
            name="test",
            description="test_description"
        )
        sports_club = SportsClub.objects.create(
            name="Test",
            address="Test",
            city="Test",
            swimming_pool=True
        )

        username = "admin"
        password = "test123"
        first_name = "test2"
        last_name = "test3"
        experience = 1

        self.user = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            sport=sport,
            sports_club=sports_club,
            experience=experience
        )

        self.client.force_login(self.user)

    def test_private_access_granted_driver(self):
        response = self.client.get(TRAINER_URL)

        trainers = get_user_model().objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["trainer_list"]),
            list(trainers)
        )
        self.assertTemplateUsed(response, "club/trainer_list.html")

    def test_private_access_granted_car(self):
        response = self.client.get(SPORTS_CLUB_URL)

        sports_clubs = SportsClub.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["sports_club_list"]),
            list(sports_clubs)
        )
        self.assertTemplateUsed(response, "club/sports_club_list.html")

    def test_private_access_granted_manufacturer(self):
        response = self.client.get(SPORT_URL)

        sports = Sport.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["sport_list"]),
            list(sports)
        )
        self.assertTemplateUsed(response, "club/sport_list.html")

    def test_private_access_granted_home(self):
        response = self.client.get(HOME)

        self.assertEqual(response.status_code, 200)

    def test_private_access_granted_login(self):
        response = self.client.get(LOGIN)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
