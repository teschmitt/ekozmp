from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import Shop


class ShopList(ListView):
    model = Shop


class ShopProductListView(ListView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shop = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'shop': self.shop,
        })
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        self.shop = get_object_or_404(Shop, slug=slug)
        return self.shop.products
