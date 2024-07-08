from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, BlogPost, VersionProduct


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = self.get_queryset(*args, **kwargs)

        for product in products:
            versions = VersionProduct.objects.filter(product=product)
            active_versions = versions.filter(version_activ=True)
            if active_versions:
                product.active_version = active_versions.last().version_title
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} {phone} : {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.user_creator = user
        product.save()
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name_product)
            new_mat.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    # form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser or user == self.object.user_creator:
            return ProductForm
        elif (user.has_perm("catalog.set_published_status") and
                user.has_perm("catalog.set_description") and
                user.has_perm("catalog.set_category_id")):
            return ProductModeratorForm
        raise PermissionDenied

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name_product)
            new_mat.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'publication_sign')
    success_url = reverse_lazy('catalog:blogpost')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'publication_sign')
    success_url = reverse_lazy('catalog:blogpost')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blogpost_detail', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blogpost')
