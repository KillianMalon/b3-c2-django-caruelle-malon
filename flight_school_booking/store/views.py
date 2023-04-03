from django.shortcuts import render
from .models import User, FlightSchool, Booking

# Create your views here.

def index(request):
    flight_schools = FlightSchool.objects.filter(available=True).order_by('reference')
    context = {'flight_schools': flight_schools}
    return render(request, 'store/index.html', context)

def listing(request):
    flight_schools = FlightSchool.objects.all().order_by('reference')
    context = {'flight_schools': flight_schools}
    return render(request, 'store/listing.html', context)