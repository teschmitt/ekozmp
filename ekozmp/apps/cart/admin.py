from django.contrib import admin
from . import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('profile', 'active', 'timestamp',)
    list_display_links = ('profile', 'active', 'timestamp',)
    search_fields = []


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'seller_product', 'product_variant', 'quantity', 'timestamp',)
    list_display_links = ('cart', 'seller_product', 'product_variant', 'quantity',)
    search_fields = []
