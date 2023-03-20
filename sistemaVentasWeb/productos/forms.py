from django import forms
from .models import Product

class ProductosForm(forms.ModelForm):
    
    class Meta:
        model = Product        
        fields = ('code','name','description','stock','image','price','available','category_product')     
        labels = {'Codigo':'Nombre','Descripción':'Stock','Imagen':'Precio','Disponibilidad':'Categoría'}
        widgets = {
            'code':forms.TextInput(attrs={'class':'form-control','placeholder':'Codigo'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}) ,
            'stock':forms.Textarea(attrs={'class':'form-control','placeholder':'stock'}) ,
            
            'price':forms.Textarea(attrs={'class':'form-control','placeholder':'precio'}) ,
            'available':forms.CheckboxInput(attrs={'class':'form-control'}) ,
            'category_product':forms.Select(attrs={'class':'form-control'}),
        }