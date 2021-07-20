from typing import ValuesView
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('items/<slug:slug>/', views.product_detail, name='product')
    
]