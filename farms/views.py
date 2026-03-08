from django.shortcuts import render
from .models import Farm

def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'farms/farm_list.html', {'farms': farms})