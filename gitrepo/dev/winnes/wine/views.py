from django.shortcuts import get_object_or_404, render
from .models import Product


def index(request):
    product=Product.objects.all()
    return render(request, 'index.html', {'product':product})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug )
    return render(request, 'product_detail/detail.html',{'product':product})