from django.apps import AppConfig


class MarketConfig(AppConfig):
    name = 'ekozmp.apps.market'

    def ready(self):
        import ekozmp.apps.market.signals
