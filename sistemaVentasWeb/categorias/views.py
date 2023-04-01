from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from categorias.models import category
from categorias.forms import CategoryForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class Categories_view(ListView):
    template_name='categorias/categorias.html'
    model = category
    

class create_category_view(CreateView):
    template_name='categorias/form-category.html'
    form_class = CategoryForm
    model = category
    success_url=reverse_lazy('categorias:categories_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'new'
        return context
    
class update_category_view(UpdateView):
    template_name='categorias/form-category.html'
    form_class = CategoryForm
    model = category
    success_url=reverse_lazy('categorias:categories_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'edit'
        return context
    
class delete_category_view(DeleteView):
    template_name='categorias/form-category.html'
    model = category
    success_url=reverse_lazy('categorias:categories_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'trash'
        return context
    
def detail_category_view(request,id_category):
    listado_productos = Product.objects.filter(category_product=id)
    category_name = get_object_or_404(category, pk=id_category)
    quantity_products = category_name.producto_set.count()
    return render(request,'categorias:detail_category',
                  {'pk':id,'listado_productos':listado_productos,
                   'quantity_products':quantity_products,
                   'gestion': 'detail'})