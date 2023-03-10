from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main.models import User
from django.urls import reverse_lazy

# Create your views here.

class usuarios_View(ListView):
    template_name='usuarios/usuarios.html'
    model = User
    

class create_user_view(CreateView):
    template_name='usuarios/form-user.html'
    fields = ['first_name','last_name','email','password','role']
    model = User
    
    
class update_user_view(UpdateView):
    template_name='usuarios/form-user.html'
    fields = ['first_name','last_name','email','password','role']
    model = User
    success_url=reverse_lazy('usuarios')
    
    
class delete_user_view(DeleteView):
    model = User
    