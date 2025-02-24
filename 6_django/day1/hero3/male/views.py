from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def boy(request):
    return HttpResponse('<p>Hello boys</p>')

def men(request):
    return HttpResponse('<p>men</p>')