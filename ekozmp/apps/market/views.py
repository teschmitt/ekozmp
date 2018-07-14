
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden
from django.urls import reverse

from django.views import View
from django.views.generic import ListView, DetailView


from ekozmp.apps.market.models import Shop, SellerProduct
from ekozmp.apps.cart.views import add_to_cart_success
from ekozmp.apps.cart.forms import AddToCartForm


class ShopList(ListView):
    model = Shop


class ShopProductList(ListView):

    '''
    Display all SellerProducts in the Shop
    context object gets passed as 'products'
    '''

    model = SellerProduct
    context_object_name = 'products'

    def get_queryset(self):
        slug = self.kwargs.get('shop_slug', None)
        return SellerProduct.objects.filter(shop__slug=slug)


class ShopProductDisplay(DetailView):

    model = SellerProduct
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, object, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'add_to_cart_form': AddToCartForm(product=object),
        })
        return context


class ShopProductDetail(View):

    '''
    More on combining Forms in Detailviews here
    https://docs.djangoproject.com/en/2.0/topics/class-based-views/mixins/#using-formmixin-with-detailview
    '''

    def get(self, request, *args, **kwargs):
        view = ShopProductDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return add_to_cart_success(request, *args, **kwargs)

