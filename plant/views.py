from django.shortcuts import render

from .models import Plant

def plant_home(request):
    plants = Plant.objects.all()
    return render(request, 'plant/home.html', {'plants':plants})

