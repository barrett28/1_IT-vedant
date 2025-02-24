from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sky(request):
    return HttpResponse("sky is up")
