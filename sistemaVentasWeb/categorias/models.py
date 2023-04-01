from django.db import models

# Create your models here.
class category(models.Model):
    name_category = models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
        
    def __str__(self):
        return self.name_category