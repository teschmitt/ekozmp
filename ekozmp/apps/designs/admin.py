from django.contrib import admin
from . import models


@admin.register(models.Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'timestamp', 'active',)
    list_display_links = ('owner', 'name',)
    search_fields = ['name']
