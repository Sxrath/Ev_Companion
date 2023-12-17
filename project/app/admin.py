from django.contrib import admin
from .models import Feedback, Location, Chargingspot,Reservation,Post,Reply

admin.site.register(Location)
admin.site.register(Chargingspot)
admin.site.register(Reservation)
admin.site.register(Feedback)
admin.site.register(Post)
admin.site.register(Reply)