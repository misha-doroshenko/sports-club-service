from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime


class Sport(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    sport_avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="sports_avatars",
        default="default.png"
    )

    def __str__(self):
        return self.name


class SportsClub(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    swimming_pool = models.BooleanField()
    club_avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="clubs_avatars",
        default="default.png"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_club"
            )
        ]

    def __str__(self):
        return self.name


class Trainer(AbstractUser):
    sports_club = models.ForeignKey(
        SportsClub,
        on_delete=models.SET_NULL,
        null=True,
        related_name="trainers"
    )
    sport = models.ForeignKey(
        Sport,
        on_delete=models.SET_NULL,
        related_name="trainers",
        null=True
    )
    trainer_avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="trainers_avatars",
        default="default.png"
    )
    experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "trainer"
        verbose_name_plural = "trainers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Workout(models.Model):
    HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(6, 24)]
    WEEKDAY_CHOICES = (
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday"),
        ("Sat", "Saturday"),
        ("Sun", "Sunday"),
    )

    sport = models.ForeignKey(
        Sport,
        on_delete=models.SET_NULL,
        related_name="workouts",
        null=True
    )
    weekday = models.CharField(max_length=3, choices=WEEKDAY_CHOICES)
    beginning_time = models.TimeField(choices=HOUR_CHOICES)
    ending_time = models.TimeField(choices=HOUR_CHOICES)
    trainer = models.ManyToManyField(Trainer, related_name="workouts")

    class Meta:
        ordering = ["sport"]
