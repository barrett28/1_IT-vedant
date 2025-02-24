from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>This is home page</h1>')
def about(request):
    return HttpResponse('<h1>This is about page</h1>')
def contact(request):
    return HttpResponse('<h1>This is contact page</h1>')