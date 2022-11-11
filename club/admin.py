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


admin.site.register(Workout)
admin.site.register(SportsClub)
admin.site.register(Sport)
