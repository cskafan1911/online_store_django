from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('info/<slug>/', BlogDetailView.as_view(), name='blog_info'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]
