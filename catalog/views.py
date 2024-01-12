from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductsForm
from catalog.models import Products, Category
from version.forms import VersionForm
from version.models import Version


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Товары для спорта'
    }

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['object_list'] = Products.objects.filter(is_published=True)
        for object in context_data['object_list']:
            version_active = Version.objects.filter(product=object, version_status=True).last()
            if version_active:
                object.version_number = version_active.version_number
                object.version_name = version_active.version_name
            else:
                object.version_number = None

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

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductsUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Введите информацию о товаре',
    }

    def get_success_url(self):
        return reverse('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Products, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)


class ProductsDetailView(DetailView):
    model = Products


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:index')
