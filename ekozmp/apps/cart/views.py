from django.shortcuts import render


# from django.views.generic.detail import SingleObjectMixin
# from django.views.generic import FormView

from ekozmp.apps.market.models import SellerProduct
from ekozmp.apps.cart.models import Cart, CartItem
from ekozmp.apps.cart.forms import AddToCartForm



def add_to_cart_success(request, *args, **kwargs):
    if request.method == 'POST':
        slug = kwargs.get('product_slug', None)
        seller_product = SellerProduct.objects.get(slug=slug)
        form = AddToCartForm(request.POST, product=seller_product)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            options = {k.split('_')[1]: v for k, v in form.cleaned_data.items() if 'option' in k}
            product_variant = seller_product.get_product_variant(options)
            cart_id = request.session.get('cart_id', None)
            try:
                cart = Cart.objects.get(id=cart_id, active=True)
            except Cart.DoesNotExist:
                cart = Cart()
                cart.save()
                request.session['cart_id'] = cart.id
                request.session.modified = True
            if seller_product and product_variant:
                cart_item, created = CartItem.objects.get_or_create(
                    cart=cart,
                    sellerproduct=seller_product,
                    product_variant=product_variant)
                if created:
                    cart_item.quantity = quantity
                else:
                    cart_item.quantity += quantity
                cart_item.save()

        else:
            print('FORM INVALID MOFO!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        return render(
            request,
            'market/sellerproduct_detail.html',
            {'add_to_cart_form': form,
             'product': seller_product,
             'shop': seller_product.shop})
