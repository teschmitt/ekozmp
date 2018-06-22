# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    profile = models.ForeignKey('accounts.Profile', null=True,
                                blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    brand = models.ForeignKey('Brand', null=True, related_name="product_brand", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        ordering = ['-order']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def get_price(self):
        if self.sale_price:
            return self.sale_price
        else:
            return self.price

    def get_featured_image(self):
        try:
            images = self.productimage_set.all()
        except:
            return None

        for i in images:
            if i.featured_image:
                return i.image
            else:
                return None

    def is_active(self):
        return self.active


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/image/")
    title = models.CharField(max_length=120, null=True, blank=True)
    featured_image = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.title)


class ProductVariation(models.Model):
    VAR_CATEGORIES = (
        ('size', _('Size')),
        ('color', _('Color')),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # token = models.CharField(default=token_generator, max_length=20, unique=True, editable=False)
    category = models.CharField(max_length=10, choices=VAR_CATEGORIES)
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    discount = models.DecimalField(blank=True, null =True, decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField(null=True, blank=True)
    sales_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    # image = models.ImageField(upload_to='products/images/')

    class Meta:
        verbose_name = _('Variation')
        verbose_name_plural = _('Variations')

    def __str__(self):
        return '{0} of {1} from {2}' .format(
            self.product.name_of_product, self.title,
            self.product.store.name_of_store)


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='products/brand/images/')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name
