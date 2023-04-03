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

def detail(request, flight_school_id):
    flight_school = FlightSchool.objects.get(pk=flight_school_id)
    context = {
        'flight_school_name': flight_school.name,
        'flight_school_picture': flight_school.picture,
        'flight_school_location': flight_school.location,
        'flight_school_id': flight_school.id,
        'flight_school_available': flight_school.available,
    }
    return render(request, 'store/detail.html', context)
