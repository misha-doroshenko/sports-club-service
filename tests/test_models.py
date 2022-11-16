from unittest import TestCase

from django.contrib.auth import get_user_model

from club.models import Sport, SportsClub


class ModelsTest(TestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name="test_sport", description="test_description")
        self.sports_club = SportsClub.objects.create(
            name="Test",
            address="Test",
            city="Test",
            swimming_pool=True
        )
        self.sport.save()
        self.sports_club.save()

        username = "admin"
        password = "test123"
        first_name = "test2"
        last_name = "test3"
        experience = 1

        self.trainer = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            sport=self.sport,
            sports_club=self.sports_club,
            experience=experience
        )
        self.trainer.save()

    def tearDown(self):
        self.trainer.delete()
        self.sport.delete()
        self.sports_club.delete()

    def test_sport_str(self):
        self.assertEqual(
            str(self.sport),
            self.sport.name
        )

    def test_sports_club_str(self):
        self.assertEqual(str(self.sports_club), self.sports_club.name)

    def test_trainer_str(self):
        self.assertEqual(
            str(self.trainer),
            f"{self.trainer.username} ({self.trainer.first_name} {self.trainer.last_name})"
        )

