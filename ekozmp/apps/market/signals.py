from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils.text import slugify

from ekozmp.apps.market.models import SellerProduct, Shop


@receiver(pre_save, sender=SellerProduct)
@receiver(pre_save, sender=Shop)
def pre_save_force_unique_slug(sender, instance, *args, **kwargs):
    # so URLs don't change: only set slug if it is empty
    if not instance.slug or len(instance.slug) == 0:
        slug = slugify(instance.name)
        unique_slug = slug
        num = 2
        while instance.__class__._default_manager.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        instance.slug = unique_slug
