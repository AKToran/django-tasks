from django.shortcuts import render
from cars.models import Cars
from brands.models import Brands

def home(request, brand_slug = None):
    if brand_slug is not None:
        brand = Brands.objects.get(slug = brand_slug)
        cars = Cars.objects.filter(brand=brand)

    else:
        cars = Cars.objects.all()
    
    brands = Brands.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands}) 