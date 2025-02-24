from django.shortcuts import render, redirect
from .forms import MarvelForms

# Create your views here.

def index(request):
    if request.method == 'POST':
        mf = MarvelForms(request.POST)
        if mf.is_valid():
            print(f'name is {mf.cleaned_data['name']}')
            print(f'hero name is {mf.cleaned_data['heroic_name']}')
            return redirect('/')
    else:
        mf = MarvelForms()
    return render(request, 'core/index.html', {'mf':mf})
