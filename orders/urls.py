from django.contrib import admin
from django.urls import path
from .views import CartDetailView, CartItemUpdate

app_name = 'orders'

urlpatterns = [
    path('cart_detail/', CartDetailView.as_view(), name='cart-detail'),
    path('cart_update/', CartItemUpdate.as_view(), name='cart-update'),
]
