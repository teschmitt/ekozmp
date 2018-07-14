from django.shortcuts import render


# from django.views.generic.detail import SingleObjectMixin
# from django.views.generic import FormView

from ekozmp.apps.market.models import SellerProduct
from ekozmp.apps.cart.models import CartItem
from ekozmp.apps.cart.forms import AddToCartForm



def add_to_cart_success(request, *args, **kwargs):
    if request.method == 'POST':
        slug = kwargs.get('product_slug', None)
        seller_product = SellerProduct.objects.get(slug=slug)
        form = AddToCartForm(request.POST, product=seller_product)

        if form.is_valid():
            fcd = form.cleaned_data
            quantity = fcd['quantity']
            options = {k.split('_')[1]: v for k, v in fcd.items() if 'option' in k}
            product_variant = seller_product.get_product_variant(options)
        else:
            print('FORM INVALID MOFO!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        return render(
            request,
            'market/sellerproduct_detail.html',
            {'add_to_cart_form': form})



# class AddToCartSuccess(SingleObjectMixin, FormView):

#     template_name = 'market/sellerproduct_detail.html'
#     form_class = AddToCartForm
#     model = CartItem
#     # slug_url_kwarg = 'product_slug'
#     # context_object_name = 'product'

#     def __init__(self, *args, **kwargs):
#         print(f'Success __init__: dir of self: {dir(self.post)}')
#         self.product = kwargs.pop('product_slug', None)
#         super().__init__(*args, **kwargs)

#      # def get_form(self, form_class=None):

#     def get_context_data(self, object, **kwargs):
#         print(f'CARTSUCCESS: {object}, {kwargs}, {dir(self)}')
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'add_to_cart_form': AddToCartForm(instance=object),
#         })
#         return context

#     # def get_form(self, form_class=None):
#     #     print('Getting the FORM')
#     #     return SellerProductForm(product=self.product)
