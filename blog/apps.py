from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Класс конфигурации Django для приложения Blog.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
