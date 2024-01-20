from django import forms

from catalog.forms import StyleFormMixin
from order.models import Order


class OrderForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для форм приложения Order.
    """

    class Meta:
        model = Order
        exclude = ('closed',)
