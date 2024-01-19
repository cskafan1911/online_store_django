from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """
    Класс конфигурации Django для приложения Catalog.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
