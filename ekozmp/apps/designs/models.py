from django.db import models
from ekozmp.apps.accounts.models import Profile


class Design(models.Model):
    owner = models.ForeignKey(
        Profile, null=False, blank=False, on_delete=models.CASCADE,
        related_name='designs')
    name = models.CharField(max_length=120, blank=False, null=False)
    asset = models.ImageField(
        upload_to='ekozmp/static/img/site/designs/', blank=True)
