from django.urls import path
from . import views 
urlpatterns=[
 path('',views.home, name='home'),
  #path converters
 # iint: numbers
 # str: string
 # path: whole urls /
 # slug: hypens and undesocres
 #uuid:universally_unique_identifer
 path('<int:year>/<str:month>',views.home, name='home'),
 path('events', views.all_events, name ='list-events')
]