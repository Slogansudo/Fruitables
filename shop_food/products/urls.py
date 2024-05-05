from django.urls import path
from .views import ProductListView, ProductDetailView, CartView

urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shopping'),
    path('shop/detail/<int:id>/', ProductDetailView.as_view(), name='shop-detail'),
    path('cart/<int:id>/detail', CartView.as_view(), name='cart')
]
