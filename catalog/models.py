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


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок", help_text="Введите название записи блога")
    slug = models.CharField(max_length=150, verbose_name="челевекочитаемая ссылка", null=True, blank=True)
    content = models.TextField(verbose_name="содержимое", help_text="Введите содержимое блога")
    image = models.ImageField(upload_to='blog_image/', verbose_name="превью (изображение)", null=True, blank=True,
                              help_text="Загрузите изображение блога")
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    publication_sign = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return f'{self.title} {self.publication_sign}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['created_at']


class VersionProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version', null=True, blank=True)
    version_number = models.IntegerField(verbose_name="номер версии", help_text="введите номер версии")
    version_title = models.CharField(max_length=20, verbose_name="название версии", help_text="введитие название версии")
    version_activ = models.BooleanField(default=False, verbose_name='Признак отображение на сайте')

    def __str__(self):
        if self.version_activ:
            v_activ = 'активный'
        else:
            v_activ = 'не активный'
        return f'{self.version_title} {v_activ}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ['version_activ']
