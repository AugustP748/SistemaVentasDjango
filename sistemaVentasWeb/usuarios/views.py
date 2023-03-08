from django.shortcuts import render
from django.views.generic import ListView, CreateView
from main.models import User
# Create your views here.
class usuarios_View(ListView):
    template_name='usuarios/usuarios.html'
    model = User
    
class create_user_view(CreateView):
    template_name='usuarios/create-user.html'
    fields = ['first_name','last_name','email','role']
    model = User