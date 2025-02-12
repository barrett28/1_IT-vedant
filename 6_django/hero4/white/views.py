from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def milk(request):
    return HttpResponse("<h1>milk is white</h1>")
def sugar(request):
    return HttpResponse("<h1>white sugar</h1>")