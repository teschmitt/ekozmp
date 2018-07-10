from django.urls import path, include
# from django.conf.urls.i18n import i18n_patterns

from .views import ShopList, ShopProductListView, ShopProductDetailView

urlpatterns = [
    path('', ShopList.as_view(), name='shop_list'),
    path('<slug:shop_slug>/', include([
        path('', ShopProductListView.as_view(), name='shopproduct_list'),
        path('product/<slug:product_slug>/',
             ShopProductDetailView.as_view(), name='shopproduct_detail'),
    ]))
]
