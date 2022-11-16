from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Sport,
    SportsClub,
    Trainer,
    Workout,
)


@admin.register(Trainer)
class TrainerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("sports_club", "sport",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("sports_club", "sport", "experience", "trainer_avatar",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "sports_club",
                        "sport",
                        "experience",
                        "trainer_avatar",
                    )
                },
            ),
        )
    )


@admin.register(SportsClub)
class SportsClubAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "address")
    search_fields = ("name",)
    list_filter = ("city",)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("sport", "weekday", "beginning_time", "ending_time")
    search_fields = ("sport",)
    list_filter = ("weekday", "sport")


admin.site.register(Sport)
