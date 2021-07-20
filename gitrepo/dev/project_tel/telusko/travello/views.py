from .models import Destinations
from django.shortcuts import render
from django.shortcuts import render   
from django.http import HttpResponse, request  

def index(request):
    dest1 = Destinations
    dest1.name = 'Kampala'
    dest1.desc = 'good'
    dest1.img = 'destination_1.jpg'
    dest1.price = 400000
    dest1.offer = False
    
    dest2 = Destinations
    dest2.name = 'Kable'
    dest2.desc = 'good'
    dest2.img = 'destination_2.jpg'
    dest2.price = 5000
    dest2.offer =True
    

    dest3 = Destinations
    dest3.name = 'Jinja'
    dest3.desc = 'good'
    dest3.img = 'destination_3.jpg'
    dest3.price =300000
    dest3.offer = False
    dests = [dest1,dest2,dest3]
    
    return render(request,'index.html',{'dests':dests})


