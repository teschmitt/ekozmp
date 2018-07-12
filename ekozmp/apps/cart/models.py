from django.db import models

from ekozmp.apps.accounts.models import Profile
from ekozmp.apps.market.models import SellerProduct
from ekozmp.apps.inventory.models import ProductVariant


class Cart(models.Model):
    profile = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sellerproduct = models.ForeignKey(SellerProduct, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


