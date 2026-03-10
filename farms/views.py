from django.shortcuts import render, get_object_or_404
from .models import Farm, Product

SITE_AUTHORS = [
    'Danylo Dudar',
    'Denys Maksymov',
    'Vasileios Papakostas',
    'Ilja Solovejs',
]

SITE_REFERENCES = [
    'J. McKenna, "CSC1025 Group Project Specification," Dublin City University, 2026.',
    'W3C Web Accessibility Initiative, "Tips on Designing for Web Accessibility," W3C, 2024. [Online]. Available: https://www.w3.org/WAI/tips/designing/',
    'Brookfield Farm, "Brookfield Farm," [Online]. Available: https://www.brookfield.farm/',
    'The Happy Pear, "Happy Pear Farm," [Online]. Available: https://farm.thehappypear.ie/people/happy-pear-farm',
]


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
    organic_filter = request.GET.get('organic')
    if organic_filter == 'true':
        products = products.filter(is_organic=True)
    return render(request, 'farms/farm_detail.html', {'farm': farm, 'products': products, 'organic_filter': organic_filter})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'farms/product_detail.html', {'product': product})

def request_info(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
    return render(request, 'request_info.html', {'submitted': submitted})


def about(request):
    return render(request, 'about.html', {
        'authors': SITE_AUTHORS,
        'references': SITE_REFERENCES,
    })


def references(request):
    return render(request, 'references.html', {
        'all_references': SITE_REFERENCES,
        'authors': SITE_AUTHORS,
        'references': [],
    })


def plot_calculator(request, length, width, yield_per_m2):
    area = length * width
    estimated_yield = area * yield_per_m2

    if yield_per_m2 <= 2:
        crop_suggestion = 'Wheat or Barley'
    elif yield_per_m2 <= 5:
        crop_suggestion = 'Potatoes or Carrots'
    else:
        crop_suggestion = 'Lettuce or Spinach'

    return render(request, 'plot_calculator.html', {
        'length': length,
        'width': width,
        'yield_per_m2': yield_per_m2,
        'area': area,
        'estimated_yield': estimated_yield,
        'crop_suggestion': crop_suggestion,
    })