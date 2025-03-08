from django.views.generic import ListView, CreateView, DeleteView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_read.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = '/'
