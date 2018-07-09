from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from ekozmp.apps.market.models import Shop, SellerProduct


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
        slug = self.kwargs.get('shop_slug', None)
        self.shop = get_object_or_404(Shop, slug=slug)
        return self.shop.products


class ShopProductDetailView(DetailView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shop = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'shop': self.shop,
        })
        return context

    def get_object(self, queryset=None):
        product_slug = self.kwargs.get('product_slug', None)
        shop_slug = self.kwargs.get('shop_slug', None)
        self.shop = get_object_or_404(Shop, slug=shop_slug)
        return get_object_or_404(SellerProduct, slug=product_slug)
