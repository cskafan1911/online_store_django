from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm
from blog.models import Blog
from config import settings


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Класс для создания блога.
    """

    model = Blog
    form_class = BlogForm
    permission_required = 'blog.blog_custom_perm'
    success_url = reverse_lazy('blog:blogs')

    def form_valid(self, form):
        """
        Метод переводит название блогов в slug.
        """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Класс для редактирования блога.
    """

    model = Blog
    form_class = BlogForm
    permission_required = 'blog.blog_custom_perm'

    def form_valid(self, form):
        """
        Метод переводит название блогов в slug.
        """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        """
        Метод перенаправляет пользователя на блог, после его редактирования и сохранения.
        """
        return reverse('blog:blog_info', args=[self.kwargs.get('slug')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для удаления блога.
    """

    model = Blog
    success_url = reverse_lazy('blog:blogs')


class BlogListView(ListView):
    """
    Класс для отображения на странице всех созданных блогов.
    """

    model = Blog
    extra_context = {
        'title': 'Блоги'
    }

    def get_queryset(self, *args, **kwargs):
        """
        Метод для получения данных о модели Blog.
        """
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.has_perm('blog.blog_custom_perm') or self.request.user.is_superuser:
            return queryset
        else:
            queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    """
    Класс для отображения информации отдельного блога.
    """

    model = Blog

    def get_object(self, queryset=None):
        """
        Метод отправляет по электронной почте оповещение о достижении 100 просмотров у блога.
        """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        if self.object.view_count == 100:
            send_mail(
                subject='Сообщение о количестве просмотров',
                message=f'У блога {self.object.title} количество просмотров достигло числа 100',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['dronov9@yandex.ru'],
            )

        return self.object
