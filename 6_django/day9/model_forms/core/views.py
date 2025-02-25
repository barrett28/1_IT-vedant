from django.shortcuts import render, redirect
from .models import MarvelModel, DcModel
from .forms import MarvelForms, DcForms
# Create your views here.

def index(request):
    if request.method == 'POST':
        mf = MarvelForms(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/')
    else:
        mf = MarvelForms()
    return render(request, 'core/index.html', {'mf':mf})


def Dc(request):
    if request.method == 'POST':
        mf = DcForms(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/dc/')
    else:
        dc = DcForms()
    return render(request, 'core/dc.html', {'dc':dc})
        

def details(request):
    mf = MarvelModel.objects.all()
    dc = DcModel.objects.all()
    
    context = {
        "mf": mf,
        "dc": dc
        
    }
    
    return render(request, 'core/details.html',context)

