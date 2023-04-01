from django import forms
from .models import category

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = category        
        fields = ('name_category',)     
        labels = {'name_category':'Categoría'}
        widgets = {
            'name_category': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Categoría'})  
        }