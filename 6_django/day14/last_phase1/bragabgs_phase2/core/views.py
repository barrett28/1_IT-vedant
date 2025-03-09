from django.shortcuts import render
from .models import Luggage

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def product(request, id):
    sc = Luggage.objects.get(pk = id)
    return render(request, 'core/product.html', {"sc":sc})

def suit_category(request):
    sc = Luggage.objects.filter(category='SUITCASE')
    return render(request,'core/suitcategory.html',{'sc':sc})


def backpack_category(request):
    sc = Luggage.objects.filter(category='BAGPACKS')
    return render(request,'core/backpackcat.html',{'sc':sc})


def dufflecat(request):
    sc = Luggage.objects.filter(category='DUFFLE')
    return render(request,'core/backpackcat.html',{'sc':sc})

def briefcase(request):
    sc = Luggage.objects.filter(category='BRIEFCASE')
    return render(request,'core/briefcasecat.html',{'sc':sc})
