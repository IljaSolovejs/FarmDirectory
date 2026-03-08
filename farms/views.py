from django.shortcuts import render
from .models import Farm

def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'farms/farm_list.html', {'farms': farms})

def home(request):
    return render(request, 'home.html')

def request_info(request):
    return render(request, 'request_info.html')

def references(request):
    return render(request, 'references.html')

def about(request):
    return render(request, 'about.html')