from django.contrib import admin
from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'timestamp', 'active',)
    list_display_links = ('owner', 'name',)
    search_fields = ['name']


@admin.register(models.SellerProduct)
class SellerProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'shop', 'base', 'design', 'timestamp', 'active',)
    list_display_links = ('name', 'owner', 'shop',)
    search_fields = ['name', 'shop']
