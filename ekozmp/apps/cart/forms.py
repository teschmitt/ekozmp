from django.forms import Form, ModelForm, ChoiceField

from ekozmp.apps.cart.models import CartItem
from ekozmp.apps.market.models import SellerProduct


class AddToCartForm(ModelForm):

    def __init__(self, *args, **kwargs):
        # print(f'CARTFORM: \n--object: {dir(object)}\n-- kwargs: {kwargs}\n-- self: {dir(self)}')
        product = kwargs.pop('product', None)
        print(f'got instance: {product}')
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update(stlye='width: 1em;')
        for option_name, option_values in product.options.items():
            option_tuple = [('', '')] + [(o.lower(), o) for o in option_values]
            self.fields[f'option_{option_name.lower()}'] = ChoiceField(
                choices=option_tuple,
                initial='',
                label=option_name)

    class Meta:
        model = CartItem
        fields = ['quantity', ]
