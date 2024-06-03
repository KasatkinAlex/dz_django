from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.models import Product, BlogPost


class ProductListView(ListView):
    model = Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} {phone} : {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'publication_sign')
    success_url = reverse_lazy('catalog:blogpost')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'publication_sign')
    success_url = reverse_lazy('catalog:blogpost')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blogpost')
