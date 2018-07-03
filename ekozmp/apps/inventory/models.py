# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(
        upload_to='ekozmp/static/img/site/brands/', blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class InventoryProduct(models.Model):
    name = models.CharField(max_length=180)
    brand = models.ForeignKey(
        Brand, null=True, related_name="inventory_products",
        on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.brand}: {self.name}'

    class Meta:
        verbose_name = _('Inventory Product')
        verbose_name_plural = _('Inventory Products')

    def is_active(self):
        return self.active


class ProductVariant(models.Model):
    sku = models.CharField(max_length=20, null=False, blank=False, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.sku


class ProductOption(models.Model):
    name = models.CharField(
        max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class ProductOptionValue(models.Model):
    product = models.ForeignKey(
        InventoryProduct, on_delete=models.CASCADE,
        related_name='product_option_values')
    option = models.ForeignKey(
        ProductOption, on_delete=models.CASCADE,
        related_name='product_option_values')
    value = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f'{self.option.name}: {self.value}'

    class Meta:
        unique_together = ('product', 'option', 'value',)


class ProductVariantValue(models.Model):
    product = models.ForeignKey(
        InventoryProduct, on_delete=models.CASCADE,
        related_name='product_variant_values')
    option_value = models.ForeignKey(
        ProductOptionValue, on_delete=models.CASCADE,
        related_name='product_variant_values')
    variant = models.ForeignKey(
        ProductVariant, on_delete=models.CASCADE,
        related_name='product_variant_values')

    def __str__(self):
        return f'{self.product} - {self.option_value}: {self.variant}'

    class Meta:
        unique_together = ('product', 'variant', 'option_value',)
