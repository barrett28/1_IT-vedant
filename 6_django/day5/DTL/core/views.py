from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html', {'villian':'goblin'})

def hero(request):
    return render(request, 'core/hero.html', {'hero':['cap', 'ironman', 'thor', 'barton', 'hulk']})
