from django.core.cache import cache

from catalog.models import Category
from config.settings import CASHES_ENABLED


def get_list_cache(models_app):
    """Принимает на вход модель, проверяет его в кэш, если там нет идет в БД и записывает в кэш и отдает модель"""
    if not CASHES_ENABLED:
        return models_app.objects.all()
    key = "list_cache"
    model_list = cache.get(key)
    if model_list is not None:
        return model_list
    model_list = models_app.objects.all()
    cache.set(key, model_list)
    return model_list
