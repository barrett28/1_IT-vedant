from django.shortcuts import render, redirect
from .models import Luggage
from .forms import  AdminProfileForm, RegistrationForm, UserProfileForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def product(request, id):
    sc = Luggage.objects.get(pk = id)
    return render(request, 'core/product.html', {"sc":sc})

def suit_category(request):
    sc = Luggage.objects.filter(category='SUITCASE')
    return render(request,'core/suitcategory.html',{'sc':sc})


def backpack_category(request):
    sc = Luggage.objects.filter(category='BAGPACKS')
    return render(request,'core/backpackcat.html',{'sc':sc})


def dufflecat(request):
    sc = Luggage.objects.filter(category='DUFFLE')
    return render(request,'core/backpackcat.html',{'sc':sc})

def briefcase(request):
    sc = Luggage.objects.filter(category='BRIEFCASE')
    return render(request,'core/briefcasecat.html',{'sc':sc})

# -------------

def registration(request):
    if request.method == 'POST':
        mf = RegistrationForm(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Registration Successfull !!')
            return redirect('registration')    
    else:
        mf  = RegistrationForm()
    return render(request,'core/registration.html',{'mf':mf})
    
    
# def profile(request):
#     return render(request, 'core/profile.html')


    
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf = AdminProfileForm(request.POST,instance=request.user)
            else:
                mf = UserProfileForm(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
                messages.success(request,'Profile Updated Successfully !!')
                return redirect('profile')
        else:
            if request.user.is_superuser == True:
                mf = AdminProfileForm(instance=request.user)
            else:
                mf = UserProfileForm(instance=request.user)
        return render(request,'core/profile.html',{'name':request.user,'mf':mf})
    else:                                               
        return redirect('login')
    
    

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':     
            mf = AuthenticationForm(request, data=request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                # print(user)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            mf = AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('profile')



def user_logout(request):
    logout(request)
    return redirect('login')


def changepassword(request):                                                
    if request.user.is_authenticated:                              
        if request.method == 'POST':                               
            mf =ChangePasswordForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                messages.success(request, 'password updated successfully')
                return redirect('profile')
        else:
            mf = ChangePasswordForm(request.user)
        return render(request,'core/changepass.html',{'mf':mf})
    else:
        return redirect('login')
    
    
def cart(request):
    return render(request, 'core/cart.html')