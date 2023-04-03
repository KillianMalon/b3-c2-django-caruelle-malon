from django.shortcuts import render
from .models import User, FlightSchool, Booking
from django.contrib.auth import login


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

def search(request):
    query = request.GET.get('query')
    if not query:
        flight_schools = FlightSchool.objects.all()
    else:
        flight_schools = FlightSchool.objects.filter(name__icontains=query)
    if not flight_schools.exists():
        flight_schools = "Aucun résultats"

    title = "Résultats pour la requête %s"%query
    context = {
        'flight_schools': flight_schools,
        'Nom': title
    }
    return render(request, 'store/search.html', context)