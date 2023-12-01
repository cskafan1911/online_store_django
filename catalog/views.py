from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

from catalog.models import Products, Category


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Товары для спорта'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Products.objects.all()

        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров',
    }


class ProductsListView(ListView):
    model = Products

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Товары категории {category_item.name}'

        return context_data


class ProductsCreateView(CreateView):
    model = Products
    fields = {'name', 'description', 'image', 'price', 'category'}
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Введите информацию о товаре',
    }


class ProductsUpdateView(UpdateView):
    model = Products
    fields = {'name', 'description', 'image', 'price', 'category'}
    extra_context = {
        'title': 'Введите информацию о товаре',
    }

    def get_success_url(self):
        return reverse('catalog:index')


class ProductInfoView(TemplateView):
    template_name = 'catalog/product_info.html'
    extra_context = {
        'title': 'Товары для спорта'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Products.objects.get(pk=self.kwargs.get('pk'))
        context_data['object'] = product_item
        context_data['title'] = f'Товары категории {product_item.name}'

        return context_data


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:index')
