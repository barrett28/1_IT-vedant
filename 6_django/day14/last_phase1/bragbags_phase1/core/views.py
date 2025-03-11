from django.shortcuts import render, redirect, get_object_or_404
from .models import Luggage, Cart
from django.db.models import Sum
from .forms import  AdminProfileForm, RegistrationForm, UserProfileForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def index(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
    return render(request, 'core/index.html', {'cart_count': cart_count})


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
    
    



# ======= add to cart =====

def add_to_cart(request, id):
    if request.user.is_authenticated:
        luggage = Luggage.objects.get(pk = id)
        user = request.user
        Cart(user = user, product = luggage).save()
        return redirect('product', id)
    else:
        return redirect('login')
    

# def view_cart(request):
#     if request.user.is_authenticated:
#         cart_items = Cart.objects.filter(user=request.user)
#         return render(request, 'core/view_cart.html', {'cart_items': cart_items})
#     else:
#         return redirect('login')


def view_cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user) 
        for item in cart_items:               # total price calculation
            item.total_price = item.product.discounted_price * item.quantity
        
        return render(request, 'core/view_cart.html', {'cart_items': cart_items})
    else:
        return redirect('login')

    

def add_quantity(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart, pk=id)
        product.quantity += 1
        product.save()
        return redirect('viewcart')
    else:
        return redirect('login')
    
    
def delete_quantity(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart, pk=id)
        if product.quantity > 1:
            product.quantity -= 1
            product.save()
        return redirect('viewcart')
    else:
        return redirect('login')
    
    
def delete_cart_item(request, id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, pk=id, user=request.user)
        cart_item.delete()
        return redirect('viewcart')
    else:
        return redirect('login')