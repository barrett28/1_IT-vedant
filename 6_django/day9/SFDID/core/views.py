from django.shortcuts import render
from .forms import MarvelForms
from .models import MarvelModel

# Create your views here.

def index(request):
    if request.method == 'POST':
        mf = MarvelForms(request.POST)
        if mf.is_valid():
            f_name = mf.cleaned_data['name']
            h_name = mf.cleaned_data['heroic_name']
            print(f_name)
            print(h_name)
            MarvelModel(name = f_name, heroic_name = h_name).save()
    else:
        mf = MarvelForms()
    return render(request, 'core/index.html', {'mf': mf})


def display(request):
    mf = MarvelModel.objects.all()
    return render(request, 'core/display.html', {'mf':mf})
