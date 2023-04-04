from django import forms
from .models import Country,Province,Location,Address

class CountryForm(forms.ModelForm):
    
    class Meta:
        model = Country        
        fields = ('name_country',)     
        labels = {'name_country':'País'}
        widgets = {
            'name_country': forms.TextInput(attrs={'class':'form-control','placeholder':'País'})
        }

class ProvinceForm(forms.ModelForm):
    country = CountryForm()
    class Meta:
        model = Province        
        fields = ('name_province',)     
        labels = {'name_province':'Provincia'}
        widgets = {
            'name_province': forms.TextInput(attrs={'class':'form-control','placeholder':'Provincia'})
        }

class LocationForm(forms.ModelForm):
    province = ProvinceForm()
    class Meta:
        model = Location        
        fields = ('postal_code','name_location',)     
        labels = {'postal_code':'Codigo Postal','name_location':'Localidad'}
        widgets = {
            'postal_code': forms.NumberInput(attrs={'class':'form-control','placeholder':'Codigo Postal'}),
            'name_location': forms.TextInput(attrs={'class':'form-control','placeholder':'Localidad'})
        }  
       
       
class AddressForm(forms.ModelForm):
    location = LocationForm()
    class Meta:
        model = Address        
        fields = ('street','number','floor','apartment','location')     
        labels = {'name':'Razon Social','email':'Email','description':'Descripción',
                  'state':'Estado'}
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Razon Social'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción'}) ,
            'state':forms.CheckboxInput(attrs={'class':'form-check-input','type':'checkbox'}) 
        }

#CountryFormSet = forms.inlineformset_factory(Province, Country, form=CountryForm, extra=1)
#ProvinceFormSet = forms.inlineformset_factory(Location, Province, form=ProvinceForm, extra=1)      
#LocationFormSet = forms.inlineformset_factory(Address, Location, form=LocationForm, extra=1)

