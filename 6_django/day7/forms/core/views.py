from django.shortcuts import render
from .forms import MarvelForms


# Create your views here.

def index(request):
    
    if request.method=='POST':
        mf = MarvelForms(request.POST)
        if mf.is_valid():
            nm = mf.cleaned_data['name']
            hn = mf.cleaned_data['heroic_name']
            print(nm)
            print(hn)
            mf = MarvelForms()
    else:
        mf = MarvelForms()
    return render(request, 'core/index.html', {'mf': mf})
