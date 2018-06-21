# -*- coding: utf-8 -*-
from django.db import models


class Product(models.Model):
    profile = models.ForeignKey('accounts.Profile', null=True,
                                blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.title)

    class Meta:
        ordering = ['-order']

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
