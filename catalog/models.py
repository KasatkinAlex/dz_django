from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name="Категория", help_text='Введите категорию')
    description = models.TextField(verbose_name="Описание", help_text='Введите описание категории')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name_product = models.CharField(max_length=50, verbose_name='Наименование', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта')
    image_product = models.ImageField(upload_to='product_image/', verbose_name='Изображение', null=True, blank=True,
                                      help_text='Загрузите изображение продукта')
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Введите цену продукта')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.name_product} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name_product', 'created_at']  # Сортировка
