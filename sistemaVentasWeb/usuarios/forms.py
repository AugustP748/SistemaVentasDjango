from django import forms
from main.models import User

class UsuariosForm(forms.ModelForm):
    
    class Meta:
        model = User        
        fields = ('first_name','last_name','email','role')     
        labels = {'first_name':'Nombre','last_name':'Apellido','email':'Email','role':'Rol'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}) ,
            'role':forms.Select(attrs={'class':'form-control'}),
        }