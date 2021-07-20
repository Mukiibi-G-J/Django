from django.contrib import admin
from .models import Venue
from .models import Event
from .models import MyClubuser

admin.site.register(Venue)
admin.site.register(MyClubuser)
admin.site.register(Event)
