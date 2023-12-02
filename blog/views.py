from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'date_of_creation')
    success_url = reverse_lazy('blog:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'date_of_creation')
    success_url = reverse_lazy('blog:blogs')


class BlogDeleteView(DeleteView):
    model = Blog
    fields = ('title', 'content', 'date_of_creation')
    success_url = reverse_lazy('blog:blogs')


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блоги'
    }


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object

