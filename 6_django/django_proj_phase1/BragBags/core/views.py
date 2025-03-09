from django.shortcuts import render
from .models import Luggage
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def product(request):
    return render(request, 'core/product.html')

def suitcategory(request):
    sc = Luggage.objects.filter(category='SUITCASE')
    return render(request, 'core/suitcategory.html', {'sc':sc})
