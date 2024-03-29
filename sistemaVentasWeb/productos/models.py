from django.db import models
from categorias.models import category
# Create your models here.

class Product(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category_product = models.ForeignKey(category,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"


