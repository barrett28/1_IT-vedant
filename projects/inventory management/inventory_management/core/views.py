from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect based on role
            if user.role == 'shop_owner':
                return redirect('shop_owner_dashboard')
            elif user.role == 'supplier':
                return redirect('supplier_dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on role
                if user.role == 'shop_owner':
                    return redirect('shop_owner_dashboard')
                elif user.role == 'supplier':
                    return redirect('supplier_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('landing_page')

def landing_page(request):
    return render(request, 'core/landing_page.html')