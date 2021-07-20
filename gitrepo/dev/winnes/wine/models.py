from re import U, VERBOSE
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    img = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    description = models.TextField(max_length=225)
    price = models.IntegerField()
    sale = models.BooleanField(default=True)
    slug = models.SlugField(max_length=225, unique=True)
    
    def get_absolute_url(self):
        return reverse('store:product', args=[self.slug])
    
    
    
    def __str__(self):
        return self.name
