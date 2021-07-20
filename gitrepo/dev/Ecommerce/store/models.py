from django.db import models
from django.contrib.auth.models import   User


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=225, unique=True)
    
    
    
    class Meta:
        verbose_name_plural = 'categories'
    
    
    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    Category= models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    createed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creater')
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225, default='admin')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length= 225)
    price = models.DecimalField(max_digits=255, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now =True)
    
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
        
    def __str__(self):
        return self.title