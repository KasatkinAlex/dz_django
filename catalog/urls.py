from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView, BlogPostListView, BlogPostDetailView, \
    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('contacts/', contacts, name='contacts'),
    path('product_info/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('blogpost/', BlogPostListView.as_view(), name='blogpost'),
    path('blogpost_detail/<int:pk>', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blogpost_create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path("edit/<int:pk>", BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('delete/<int:pk>', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path("product_create/", ProductCreateView.as_view(), name='product_create'),
    path("product_update/<int:pk>", ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
