from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'date_of_creation')
    success_url = reverse_lazy('blog:')

