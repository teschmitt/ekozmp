from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ("user", "account_type", "language", "timestamp")
    search_fields = ["user__username"]

