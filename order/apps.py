from django.apps import AppConfig


class OrderConfig(AppConfig):
    """
    Класс конфигурации Django для приложения Order.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'
