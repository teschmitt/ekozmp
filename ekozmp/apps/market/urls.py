from django.urls import path
# from django.conf.urls.i18n import i18n_patterns

from .views import ShopList, ShopProductListView

urlpatterns = [
    path('', ShopList.as_view(), name='shop-list'),
    path('<int:id>/', ShopProductListView.as_view(), name='shopproduct-list'),
]
