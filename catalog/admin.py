from django.contrib import admin

from catalog.models import Category, Products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Category.
    """

    list_display = ('pk', 'name')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """
    Класс для настройки панели администратора модели Products.
    """

    list_display = ('pk', 'name', 'price', 'category', 'creator',)
    list_filter = ('category', 'creator',)
    search_fields = ('name', 'category',)
