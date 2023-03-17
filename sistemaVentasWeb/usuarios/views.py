from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main.models import User
from django.urls import reverse_lazy

from .forms import UsuariosForm

# Create your views here.

class usuarios_View(ListView):
    template_name='usuarios/usuarios.html'
    model = User
    

class create_user_view(CreateView):
    template_name='usuarios/form-user.html'
    form_class = UsuariosForm
    #fields = ['first_name','last_name','email','password','role']
    model = User
    success_url=reverse_lazy('usuarios:usurios_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'new'
        return context
    
class update_user_view(UpdateView):
    template_name='usuarios/form-user.html'
    form_class = UsuariosForm
    #fields = ['first_name','last_name','email','password','role']
    model = User
    success_url=reverse_lazy('usuarios:usurios_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'edit'
        return context
    
    
    
class delete_user_view(DeleteView):
    template_name='usuarios/form-user.html'
    model = User
    success_url=reverse_lazy('usuarios:usurios_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gestion'] = 'trash'
        return context