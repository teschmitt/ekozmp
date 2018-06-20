from django.apps import apps
from django.test import TestCase
from ..apps import AccountsConfig


class AccountsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(AccountsConfig.name, 'accounts')
        self.assertEqual(apps.get_app_config('accounts').name, 'collabd.apps.accounts')
