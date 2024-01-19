from django.core.cache import cache

from catalog.models import Category, Products
from django.conf import settings

from version.models import Version


def get_cache_objects_list(model_):
    """
    Функция кеширования списка категорий товара
    :param model_: Модель кешируемого объекта
    """
    key = 'objects_list'
    objects_list = cache.get(key)
    if settings.CACHE_ENABLED:
        if objects_list is None:
            objects_list = model_.objects.all()
            cache.set(key, objects_list)
    else:
        objects_list = model_.objects.all()

    return objects_list


def get_product_active_version(context_data):
    """
    Функция для фильтрует и выводит на экран продукты с последней активной версией.
    """
    context_data['object_list'] = Products.objects.filter(is_published=True)
    for object in context_data['object_list']:
        version_active = Version.objects.filter(product=object, version_status=True).last()
        if version_active:
            object.version_number = version_active.version_number
            object.version_name = version_active.version_name
        else:
            object.version_number = None

    return context_data
