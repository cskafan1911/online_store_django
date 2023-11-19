from django.contrib import admin

from catalog.models import Category, Products, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'category',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number',)
    search_fields = ('user_name', 'phone_number',)
