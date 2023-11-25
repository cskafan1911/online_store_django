from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, product_info, product_add

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/product_info/', product_info, name='product_info'),
    path('product_add/', product_add, name='product_add')

]
