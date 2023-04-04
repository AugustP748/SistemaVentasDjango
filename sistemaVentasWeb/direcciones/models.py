from django.db import models

# Create your models here.

class Country(models.Model):
    name_country = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    
    
class Province(models.Model):
    name_province = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        

class Location(models.Model):
    postal_code = models.IntegerField(primary_key=True)
    name_location = models.CharField(max_length=50)
    provinde = models.ForeignKey(Province, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Localities'


class Address(models.Model):
    street = models.CharField(max_length=225)
    number = models.IntegerField()
    floor = models.IntegerField(blank=True, null=True)
    apartment = models.CharField(max_length=3,blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'