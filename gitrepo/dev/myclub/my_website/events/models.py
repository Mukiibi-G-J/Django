from types import WrapperDescriptorType
from django.db import models
from django.db.models import manager
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length= 120)
    address =models.CharField(max_length=300)
    zip_code =models.CharField('Zip code', max_length=15)
    phone=models.CharField('Contact Phone', max_length=25)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')
    
    def __str__(self):
        return self.name
    

class MyClubuser(models.Model):
    frist_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email = models.EmailField('User email')
    
    def __str__ (self):
        return self.frist_name +" " +self.last_name
        
    
    
class  Event(models.Model):
    name =models.CharField('Event Name',max_length=120)
    venue = models.ForeignKey(Venue,blank=True, null=True, on_delete=models.CASCADE)
    event_date = models.DateTimeField('Event Date')
    # venue = models.CharField(max_length=120)
    manager =models.CharField(max_length=120)
    description = models.TextField(blank = True)
    attendees =  ManyToManyField(MyClubuser, blank=True)
    
    def __str__(self):
            return self.name