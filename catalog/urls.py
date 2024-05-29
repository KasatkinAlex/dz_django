from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('contacts/', contacts, name='contacts'),
    path('product_info/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
