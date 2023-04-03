from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FlightSchool(models.Model):
    name = models.CharField(max_length=200, unique=True)
    picture = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    reference = models.IntegerField(null=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flightschool = models.ForeignKey(FlightSchool, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.usernam
