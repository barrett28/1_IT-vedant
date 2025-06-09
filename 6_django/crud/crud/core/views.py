from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm

# Create your views here.


def index(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            uf.save()
            return redirect("index")
    else:
        uf = UserForm()
        um = UserModel.objects.all()
    return render(request, "core/index.html", {"uf":uf, "um":um})


def user_del(request, id):
    du = UserModel.objects.get(pk=id)
    du.delete()
    return redirect("/")

def user_upt(request, id):
    if request.method == "POST":
        um = UserModel.objects.get(pk=id)
        uf = UserForm(request.POST, instance=um)
        if uf.is_valid():
            uf.save()
            return redirect("index")
    else:
        um = UserModel.objects.get(pk=id)
        uf = UserForm(instance=um)
    
    return render(request, "core/update.html", {"um":um, "uf":uf})