from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Session(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '%s: %s - %s' % (self.date, str(self.start_time), str(self.end_time))


class Location(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return '%s' % self.name


class Route(models.Model):
    start_location = models.ForeignKey(Location, related_name='start_location')
    end_location = models.ForeignKey(Location, related_name='end_location')
    route_url = models.CharField(max_length=512)

    def __str__(self):
        return '%s - %s' % (self.start_location.name, self.end_location.name)


class Stop(models.Model):
    route = models.ForeignKey(Route)
    location = models.ForeignKey(Location)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Trip(models.Model):
    route = models.ForeignKey(Route)
    session = models.ForeignKey(Session)


class Log(models.Model):
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)
