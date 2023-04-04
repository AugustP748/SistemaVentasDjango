from django import forms
from .models import Provider
from direcciones.models import Address
from direcciones.forms import AddressForm
from categorias.models import category
from categorias.forms import CategoryForm

class ProveedoresForm(forms.ModelForm):
    address = AddressForm()
    categories = forms.ModelMultipleChoiceField(queryset=category.objects.all())
    class Meta:
        model = Provider        
        fields = ('name','email','phone','description','state','categories')     
        labels = {'name':'Razon Social','email':'Email','description':'Descripción',
                  'state':'Activo','categories':'Categorías'}
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Razon Social'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}) ,
            'state':forms.CheckboxInput(attrs={'class':'form-check-input','type':'checkbox'}),
            'categories':forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'}),
        }
        
#AdressFormSet = forms.inlineformset_factory(Provider, Address, form=AddressForm, extra=1)
#CategoryFormSet = forms.inlineformset_factory(Provider,category,form=CategoryForm,extra=1)
