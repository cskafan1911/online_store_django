from django import forms

from catalog.forms import StyleFormMixin
from order.models import Order


class OrderForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Order
        exclude = ('closed',)
