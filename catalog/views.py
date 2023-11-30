from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Products, Category


def index(request):
    products_list = Products.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Товары для спорта',
    }

    return render(request, 'catalog/index.html', context)


def product_info(request, pk):
    context = {
        'object': Products.objects.get(pk=pk),
        'title': 'Товары для спорта',
    }

    return render(request, 'catalog/product_info.html', context)


def product_add(request):

    context = {
        'title': 'Введите данные о товаре'
    }

    if request.method == 'POST':
        new_product = {
            'name': request.POST.get('product_name'),
            'description': request.POST.get('description'),
            'image': request.POST.get('image'),
            'price': request.POST.get('price'),
            'category': Category.objects.get(pk=request.POST.get('category'))
        }

        Products.objects.create(**new_product)

    return render(request, 'catalog/product_add.html', context)


# def categories(request):
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list,
#         'title': 'Категории товаров',
#     }
#
#     return render(request, 'catalog/category_list.html', context)

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров',
    }


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Products.objects.filter(category=pk),
        'category_pk': category_item.pk,
        'title': f'Товары категории {category_item.name}'
    }

    return render(request, 'catalog/category_products.html', context)

# class ProductsListView(ListView):
#     model = Products
#
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(category=self.kwargs.get('pk'))
#
#         return queryset
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#         context_data = {
#             'object_list': Products.objects.filter(category=pk),
#             'title': 'Категория'
#         }
#         return context_data

