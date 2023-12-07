from django.conf import settings
from django.core.mail import send_mail
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

    def form_valid(self, form):
        obj = form.save()
        send_mail(
            subject=f'Для товара {obj.product.name} есть заявка',
            message=f'Имя: {obj.name} ({obj.email})\nСообщение: {obj.message}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['dronov9@yandex.ru'],
        )
        return super().form_valid(form)
