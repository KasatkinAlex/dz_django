from django.core.management import BaseCommand
import json

from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', "rt", encoding="utf-8") as file:
            json_read = json.load(file)

        category_list = []
        for i in json_read:
            if i['model'] == 'catalog.category':
                category_list.append(i)
        return category_list

    @staticmethod
    def json_read_products():
        with open('catalog_data.json', "rt", encoding="utf-8") as file:
            json_read = json.load(file)

        products_list = []
        for i in json_read:
            if i['model'] == 'catalog.product':
                products_list.append(i)
        return products_list

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name_category=category['fields']['name_category'],
                         description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name_product=product['fields']['name_product'],
                        description=product['fields']['description'],
                        image_product=product['fields']['image_product'],
                        category_id=Category.objects.get(pk=product['fields']['category_id']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']
                        )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
