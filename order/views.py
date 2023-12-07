from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from catalog.models import Products
from order.models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = ('product', 'name', 'email', 'message',)

    def get_success_url(self):
        return reverse('catalog:product_info', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['product'] = get_object_or_404(Products, pk=self.kwargs.get('pk'))

        return context_data
