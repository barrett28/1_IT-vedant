from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ironman(request):
    return HttpResponse('<h1> ironman</h1>')
def spiderman(request):
    return HttpResponse('<h1> spiderman</h1>')