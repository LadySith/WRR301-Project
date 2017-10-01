from django.contrib import admin

# Register your models here.
from .models import Session, Trip, Route, Log, Stop, Location

admin.site.register(Session)
admin.site.register(Trip)
admin.site.register(Route)
admin.site.register(Log)
admin.site.register(Stop)
admin.site.register(Location)

