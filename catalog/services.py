from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_cache_objects_list(model_):

    key = 'objects_list'
    objects_list = cache.get(key)
    if CACHE_ENABLED:
        if objects_list is None:
            objects_list = model_.objects.all()
            cache.set(key, objects_list)
    else:
        objects_list = model_.objects.all()

    return objects_list
