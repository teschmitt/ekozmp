# -*- coding: utf-8 -*-

import pytz
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from timezone_field import TimeZoneField

from . import managers
from ekozmp.apps.inventory.models import InventoryProduct


"""
class MyModel(models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    # Custom Properties
    # Methods
    # Meta and String
"""


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile", verbose_name=_("user"),
                                on_delete=models.CASCADE)

    # Attributes - Mandatory
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    ACCOUNT_TYPES = (
        ('S', _('Seller')),
        ('B', _('Buyer')),
        ('X', _('Seller and Buyer'))
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    active = models.BooleanField(default=True)

    # Attributes - Optional
    language = models.CharField(max_length=10, blank=True)
    timezone = TimeZoneField(default='Europe/Berlin')
    """
    Weitere Felder:
    birthday
    accepted_dse (Datenschutzerklärung)
    accepted_cookiepolicy
    pagination_prefs - items_per_page
    """

    # Object Manager
    objects = managers.ProfileManager()

    # Custom Properties
    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    # Methods

    # Meta and String
    class Meta:
        ordering = ("user",)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


class ProfileImage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="ekozmp/static/img/profileimages/")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.title)
