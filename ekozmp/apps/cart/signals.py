from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver

from ekozmp.apps.cart.models import Cart, CartItem


@receiver([post_save, post_delete], sender=CartItem)
def update_cart_total(sender, instance, **kwargs):
    # cart = instance.cart
    # totals = [item.product.get_price() for item in cart.cartitem_set.all()]
    # cart.total = sum(totals)
    # cart.save()
    pass
