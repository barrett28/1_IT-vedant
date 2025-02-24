from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tile(request):
    return HttpResponse("<h1>black tiles</h1>")
def powder(request):
    return HttpResponse("<h1>gunpowder</h1>")
