
from threading import current_thread
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime, time
from .models import Event
def all_events(request):
    events_list = Event.objects.all()
    return render(request, 'events/events_list.html', {'event_list':events_list})
    
    
    
def home(request,year= datetime.now().year, month=datetime.now().strftime('%B')):
            # convert month from name to number
             month = month.capitalize()
             month_number = list(calendar.month_name).index(month)
             month_number = int(month_number)
            
            
            # create a calender
             cal = HTMLCalendar().formatmonth(year,month_number)
             
             
            #  Get current year
             now = datetime.now()
             current_year = now.year
             
             #Get current time
             time = now.strftime('%I:%M:%P')
             
             
             return render(request, 
            'events/home.html',{
			'first_name':'John', 
			"year":year,
			"month":month,
			"month_number":month_number,
            "cal":cal,
            "current_year": current_year,
            "time":time,
    
   
      })
