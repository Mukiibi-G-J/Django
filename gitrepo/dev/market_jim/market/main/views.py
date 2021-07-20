from django.shortcuts import render 
from django.http import HttpResponse, request  
from .models import Item

def homepage(request):
	return render(request,'main/home.html')

 
def itemspage(request):
    items = Item.objects.all()
    return render(request, 'main/items.html',{'items':items})
  
  
# def base(request):
#   return render(request, 'main/base.html')