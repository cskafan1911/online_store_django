from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
]
