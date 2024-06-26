from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, View, UpdateView
from .models import Cart, CartItem


class CartDetailView(DetailView):
    model = Cart
    template_name = 'orders/cart_detail.html'
    context_object_name = 'cart'


class CartItemUpdate(UpdateView):
    model = CartItem
    fields = ['quantity']
    template_name = 'orders/cart_update.html'
    success_url = reverse_lazy('cart_detail')

# class OrderListView(ListView):
#     model = Order
#     template_name = 'orders/order_list.html'
#     context_object_name = 'orders'
#     ordering = ['-created_time']
#
#
#
# class OrderDetailView(DetailView):
#     model = Order
#     template_name = 'orders/order_detail.html'
#     context_object_name = 'order'
#
#
#
#
# class DiscountListView(ListView):
#     model = Discount
#     template_name = 'orders/discount_list.html'
#     context_object_name = 'discounts'
#
# class DiscountDetailView(DetailView):
#     model = Discount
#     template_name = 'orders/discount_detail.html'
#     context_object_name = 'discount'
#
#     def get_context_data(self, **kwargs):
#         context = super(DiscountDetailView, self).get_context_data()
#         discount_id = kwargs['discount_id']
#         discount = Discount.objects.get(pk=discount_id)
#         context['user'] = discount.user_id
#         context['product'] = discount.product_id
#         context['doscount'] = discount
#
#         return context
