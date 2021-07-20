from django.urls import path
from .import views
urlpatterns = [
    path('' , views.contacts),
    path('snippet', views.snippet_details)
     
]
