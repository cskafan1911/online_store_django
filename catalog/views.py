from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

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
    }

    return render(request, 'catalog/product_info.html', context)


def product_add(request):

    if request.method == 'POST':
        new_product = {
            'name': request.POST.get('product_name'),
            'description': request.POST.get('description'),
            'image': request.POST.get('image'),
            'price': request.POST.get('price'),
            'category': Category.objects.get(pk=request.POST.get('category'))
        }

        Products.objects.create(**new_product)

    return render(request, 'catalog/product_add.html')
