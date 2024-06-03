from django.contrib import admin

from catalog.models import Category, Product, BlogPost


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_product', 'price', 'category_id',)
    list_filter = ('category_id',)
    search_fields = ('name_product', 'description')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_sign', 'views_count')
    search_fields = ('title', 'content')
