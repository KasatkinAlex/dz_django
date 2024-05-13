from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('contacts/', contacts, name='contacts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
