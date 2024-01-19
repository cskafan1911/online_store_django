from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductsForm, ModeratorForm
from catalog.models import Products, Category
from catalog.services import get_cache_objects_list, get_product_active_version
from version.forms import VersionForm
from version.models import Version


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Товары для спорта'
    }

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data = get_product_active_version(context_data)

        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров',
    }

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_cache_objects_list(Category)

        return context_data


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


class ProductsCreateView(LoginRequiredMixin, CreateView):
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


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy('catalog:index')
    extra_context = {
        'title': 'Введите информацию о товаре',
    }

    def get_form_class(self):
        if self.request.user.groups.filter(name='Moderator').exists():
            return ModeratorForm

        return ProductsForm

    def get_object(self, queryset=None):
        self.object = super().get_object()
        if self.request.user.groups.filter(name='Moderator').exists():
            return self.object
        elif self.object.creator != self.request.user and not self.request.user.is_superuser:
            raise Http404('Вы не можете редактировать данный товар')

        return self.object

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


class ProductsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Products
    permission_required = 'catalog.delete_products'
    success_url = reverse_lazy('catalog:index')
