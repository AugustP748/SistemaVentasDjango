from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from .models import Product
from .forms import ProductosForm
from django.urls import reverse_lazy

# Create your views here.

class products_view(ListView):
    template_name='productos/productos.html'
    model = Product

class create_product_view(CreateView):
    template_name='productos/form-product.html'
    form_class = ProductosForm
    model = Product
    success_url=reverse_lazy('productos:products_view')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'new'
        return context
    
class detail_product_view(DetailView):
    ...