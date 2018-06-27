from django.urls import path
# from django.conf.urls.i18n import i18n_patterns

from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
]
