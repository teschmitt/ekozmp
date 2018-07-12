from django.apps import AppConfig


class CartConfig(AppConfig):
    name = 'ekozmp.apps.cart'

    def ready(self):
        import ekozmp.apps.cart.signals
