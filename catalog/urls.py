from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('contacts/', contacts, name='contacts'),
    path('product_info/<int:pk>', product_info, name='product_info')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
