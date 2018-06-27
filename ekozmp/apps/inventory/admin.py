from django.contrib import admin
from . import models


@admin.register(models.InventoryProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'timestamp',)
    list_display_links = ('brand', 'name',)
    search_fields = ['name', 'brand']


@admin.register(models.ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(models.ProductOptionValue)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('product', 'option', 'value',)
    search_fields = ['value']


@admin.register(models.ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('sku', 'price',)
    # search_fields = ['name']


@admin.register(models.ProductVariantValue)
class ProductVariantValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'option_value', 'variant',)
    # search_fields = ['name']


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
