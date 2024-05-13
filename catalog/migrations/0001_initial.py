# Generated by Django 5.0.6 on 2024-05-13 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(help_text='Введите категорию', max_length=100, verbose_name='Категория')),
                ('description', models.TextField(help_text='Введите описание категории', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(help_text='Введите название продукта', max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(help_text='Введите описание продукта', verbose_name='Описание')),
                ('image_product', models.ImageField(blank=True, help_text='Загрузите изображение продукта', null=True, upload_to='product_image/', verbose_name='Изображение')),
                ('price', models.IntegerField(help_text='Введите цену продукта', verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name_product', 'created_at'],
            },
        ),
    ]
