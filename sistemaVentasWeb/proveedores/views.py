from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Provider
from .forms import ProveedoresForm

# Create your views here.
class providers_view(ListView):
    template_name='proveedores/proveedores.html'
    model = Provider
    
class create_providers_view(CreateView):
    template_name='proveedores/form-provider.html'
    form_class = ProveedoresForm
    model = Provider
    success_url=reverse_lazy('proveedores:providers_view')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'new'
        return context