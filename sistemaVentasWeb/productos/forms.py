from django import forms
from .models import Product

class ProductosForm(forms.ModelForm):
    
    class Meta:
        model = Product        
        fields = ('code','name','description','image','stock','price','available','category_product')     
        labels = {'code':'Codigo','name':'Producto','description':'Descripción','stock':'Stock',
                  'image':'Imagen','price':'Precio','available':'Disponibilidad',
                  'category_product':'Categoría'}
        widgets = {
            'code':forms.TextInput(attrs={'class':'form-control','placeholder':'Codigo'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Producto'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}) ,
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'stock','type':'number'}) ,
            'image':forms.ClearableFileInput(attrs={'class':'img-thumbnail'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'precio'}) ,
            'category_product':forms.Select(attrs={'class':'form-control'}),
            'available':forms.CheckboxInput(attrs={'class':'form-check-input','type':'checkbox'}) 
        }