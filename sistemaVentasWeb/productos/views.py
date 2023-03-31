from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Product, category
from .forms import ProductosForm, CategoryForm
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

class update_product_view(UpdateView):
    template_name='productos/form-product.html'
    form_class = ProductosForm
    model = Product
    success_url=reverse_lazy('productos:products_view')
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['gestion'] = 'edit'
            return context  

class delete_product_view(DeleteView):
    template_name='productos/form-product.html'
    model = Product
    success_url=reverse_lazy('productos:products_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'trash'
        return context

class detail_product_view(DetailView):
    template_name='productos/form-product.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'detail'
        return context

class Categories_view(ListView):
    template_name='categorias/categorias.html'
    model = category
    

class create_category_view(CreateView):
    template_name='categorias/form-category.html'
    form_class = CategoryForm
    model = category
    success_url=reverse_lazy('productos:categories_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'new'
        return context
    
class update_category_view(UpdateView):
    template_name='categorias/form-category.html'
    form_class = CategoryForm
    model = category
    success_url=reverse_lazy('productos:categories_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'edit'
        return context
    
class delete_category_view(DeleteView):
    template_name='categorias/form-category.html'
    model = category
    success_url=reverse_lazy('productos:categories_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'trash'
        return context
    
def detail_category_view(request,id):
    listado_productos = Product.objects.filter(category_product=id)
    return render(request,'productos:detail_category',{'pk':id,'listado_productos':listado_productos})