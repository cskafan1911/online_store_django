from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Order.
    """

    list_display = ('product', 'name', 'email',)
    list_filter = ('product',)

