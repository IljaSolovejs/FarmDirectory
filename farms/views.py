from django.shortcuts import render, get_object_or_404
from .models import Farm, Product


def home(request):
    farms = Farm.objects.all()
    products = Product.objects.all()
    context = {
        'farms': farms,
        'products': products,
        'farm_count': farms.count(),
        'product_count': products.count(),
    }
    return render(request, 'home.html', context)


def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'farms/farm_list.html', {'farms': farms})


def farm_detail(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    products = Product.objects.filter(farm=farm)
    return render(request, 'farms/farm_detail.html', {'farm': farm, 'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'farms/product_detail.html', {'product': product})