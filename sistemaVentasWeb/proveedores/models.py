from django.db import models
from categorias.models import category
from direcciones.models import Address

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    categories = models.ManyToManyField(category)
    description = models.TextField()
    address = models.ManyToManyField(Address)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
