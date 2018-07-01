# -*- coding: utf-8 -*-
from django.db import models
# from django.utils.translation import ugettext_lazy as _

from ekozmp.apps.inventory.models import ProductVariant
from ekozmp.apps.designs.models import Design
from ekozmp.apps.accounts.models import Profile


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


class Shop(models.Model):
    owner = models.ForeignKey(
        Profile, null=False, blank=False, on_delete=models.CASCADE,
        related_name='shops')
    name = models.CharField(max_length=120, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


class SellerProduct(models.Model):
    owner = models.ForeignKey(
        Profile, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    base = models.ForeignKey(
        ProductVariant, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    design = models.ForeignKey(
        Design, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    shop = models.ForeignKey(
        Shop, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    name = models.CharField(max_length=120, blank=False, null=False)
    markup = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
