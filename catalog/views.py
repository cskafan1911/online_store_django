from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductsForm
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
    form_class = ProductsForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Введите информацию о товаре',
    }


class ProductsUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Введите информацию о товаре',
    }

    def get_success_url(self):
        return reverse('catalog:index')


class ProductsDetailView(DetailView):
    model = Products


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:index')
