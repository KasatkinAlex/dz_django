from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
# def index(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, "catalog/product_li.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} {phone} : {message}')
    return render(request, 'catalog/contacts.html')


# def product_info(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {'product': product}
#     return render(request, "catalog/product_info.html", context)


class ProductDetailView(DetailView):
    model = Product
