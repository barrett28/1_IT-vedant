from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def product(request):
    return render(request, 'core/product.html')

def suitcategory(request):
    return render(request, 'core/suitcategory.html')
