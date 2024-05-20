from django.shortcuts import render

from catalog.models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "catalog/product_list.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} {phone} : {message}')
    return render(request, 'catalog/contacts.html')


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, "catalog/product_info.html", context)
