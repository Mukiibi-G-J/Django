from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name = 'home'),
    path('matress/', views.mattress, name='mattress')
    
]