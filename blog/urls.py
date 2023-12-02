from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductsCreateView, CategoryListView, ProductsListView, IndexView, ProductsUpdateView, \
    ProductInfoView, ProductsDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category_products/<int:pk>/', ProductsListView.as_view(), name='category_products'),
    path('products/<int:pk>/', ProductsListView.as_view(), name='product'),
    path('products/<int:pk>/info/', ProductInfoView.as_view(), name='product_info'),
    path('products/create/', ProductsCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='product_delete'),

]
