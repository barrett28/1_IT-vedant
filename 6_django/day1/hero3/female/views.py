from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def girl(request):
    return HttpResponse('<h1>Hello girls</h1>')

def women(request):
    return HttpResponse('<h1>Women</h1>')