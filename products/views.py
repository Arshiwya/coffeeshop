from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Product, Category


class CreateProductView(CreateView):
    model = Product
    template_name = 'products/create-product.html'
    fields = ['name', "sugar",
              "coffee",
              "flour",
              "chocolate",
              "categories", ]

    success_url = '/'


class UpdateProductView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'products/update-product.html'
    fields = ['name', "sugar",
              "coffee",
              "flour",
              "chocolate",
              "categories", ]

    def get_success_url(self):
        url = f'/products/update/{self.object.id}'
        return url


class DeleteProductView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/delete-product.html'
    success_url = '/'


class CreateCategoryView(CreateView):
    model = Category
    template_name = 'products/create-category.html'
    fields = ['name', ]

    def get_success_url(self):
        print(self.object.id)


class UpdateCategoryView(UpdateView):
    queryset = Category.objects.all()
    template_name = 'products/update-category.html'
    fields = ['name', ]

    def get_success_url(self):
        url = f'/products/category/update/{self.object.id}'
        return url


class DeleteCategoryView(DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'products/delete-category.html'
    success_url = '/'


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/products-list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-details.html'
    context_object_name = 'product'
