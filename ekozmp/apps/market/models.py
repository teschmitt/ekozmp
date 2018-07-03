# -*- coding: utf-8 -*-
from django.db import models
# from django.utils.translation import ugettext_lazy as _

from ekozmp.apps.inventory.models import \
     InventoryProduct, ProductVariant, ProductVariantValue
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
    slug = models.SlugField(max_length=140, unique=True, blank=True, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    @property
    def products(self):
        return self.seller_products.filter(shop=self)

    @property
    def products_count(self):
        return self.seller_products.filter(shop=self).count()

    def __str__(self):
        return f'{self.owner}: {self.name}'


class SellerProduct(models.Model):
    owner = models.ForeignKey(
        Profile, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    base = models.ForeignKey(
        InventoryProduct, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    design = models.ForeignKey(
        Design, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    shop = models.ForeignKey(
        Shop, null=False, blank=False, on_delete=models.CASCADE,
        related_name='seller_products')
    name = models.CharField(max_length=120, blank=False, null=False)
    slug = models.SlugField(max_length=140, unique=True, blank=True, null=False)
    markup = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    @property
    def display_price(self):
        p = self.base.product_variant_values.values(
            'variant__price').aggregate(models.Min('variant__price'))
        return p['variant__price__min'] + self.markup

    def __str__(self):
        return f'{self.owner}: {self.name}'
