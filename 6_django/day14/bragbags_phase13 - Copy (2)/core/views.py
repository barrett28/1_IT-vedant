from django.shortcuts import render, redirect, get_object_or_404
from .models import Luggage, Cart, CustomerDetail, Order
from django.db.models import Sum
from .forms import  AdminProfileForm, RegistrationForm, UserProfileForm, ChangePasswordForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ====paypal==
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

# ======= email forgot password====
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.http import HttpResponse


# Create your views here.

def index2(request):
    return render(request, 'core/index2.html')

def index(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
    return render(request, 'core/index.html', {'cart_count': cart_count})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')


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

# def add_to_cart(request, id):
#     if request.user.is_authenticated:
#         luggage = Luggage.objects.get(pk = id)
#         user = request.user
#         Cart(user = user, product = luggage).save()
#         return redirect('product', id)
#     else:
#         return redirect('login')

def add_to_cart(request, id):
    if request.user.is_authenticated:
        luggage = Luggage.objects.get(pk = id)
        user = request.user
        cart_item = Cart.objects.filter(user=user, product=luggage).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'{luggage.name} quantity updated in cart!')
        else:
            Cart(user=user, product=luggage).save()
            messages.success(request, f'{luggage.name} added to cart successfully!')
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


# ---------------------------------

def address(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ad = CustomerForm(request.POST)
            if ad.is_valid():
                user = request.user
                name = ad.cleaned_data['name']
                address = ad.cleaned_data['address']
                city = ad.cleaned_data['city']
                state = ad.cleaned_data['state']
                pincode = ad.cleaned_data['pincode']
                
                CustomerDetail(user=user,name=name,address=address,city=city,state=state,pincode=pincode).save()
                return redirect('address')
        else:
            ad = CustomerForm()
            address = CustomerDetail.objects.filter(user=request.user)
        return render(request, 'core/address.html', {'ad':ad, 'address':address})
    else:
        return redirect('login')
    
    
def delete_address(request,id):
        de = CustomerDetail.objects.get(pk=id)
        de.delete()
        return redirect('address')
    
    
# ---------------------

def checkout(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        total = 0
        delivery_charges = 200
        for item in cart_items:               # total price calculation
            total += (item.product.discounted_price * item.quantity)
            final_price = total+delivery_charges
        address = CustomerDetail.objects.filter(user=request.user)
        return render(request, 'core/checkout.html', {'cart_items':cart_items, 'total':total, 'final_price':final_price, 'address':address})
    
    
def payment(request):
    
    if request.method=='POST':
        selected_address_id = request.POST.get('selected_address')
        print('=========',selected_address_id)
    cart_items = Cart.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    total =0
    delivery_charge =200
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delivery_charge + total
    
    address = CustomerDetail.objects.filter(user=request.user)
    
    # ====paypal code====

    host = request.get_host()
    
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,   #This is typically the email address associated with the PayPal account that will receive the payment.
        'amount': final_price,    #: The amount of money to be charged for the transaction. 
        'item_name': 'Bag',       # Describes the item being purchased.
        'invoice': uuid.uuid4(),  #A unique identifier for the invoice. It uses uuid.uuid4() to generate a random UUID.
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",         #The URL where PayPal will send Instant Payment Notifications (IPN) to notify the merchant about payment-related events
        'return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}",     #The URL where the customer will be redirected after a successful payment. 
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",      #The URL where the customer will be redirected if they choose to cancel the payment. 
    }
    
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request, 'core/payment.html',{'paypal':paypal_payment})
    
    
def payment_success(request, selected_address_id):
    user = request.user
    address_data = CustomerDetail.objects.get(pk=selected_address_id)
    cart = Cart.objects.filter(user = request.user)
    for cart in cart:
        total_price = (cart.quantity * cart.product.discounted_price)+200
        Order(user=user,customer=address_data,quantity=cart.quantity,product=cart.product, total_price=total_price).save()
        cart.delete()
    return render(request,'core/payment_success.html')


def payment_failed(request):
    return render(request,'core/payment_failed.html')

# ==========order=======

def order(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.total_price for order in orders) 
    return render(request, 'core/order.html', {'orders': orders, 'total_price': total_price})

# ==============

def buynow(request, id):
    if request.user.is_authenticated:
        luggage = Luggage.objects.get(pk=id)
        delivery_charge = 200
        final_price = delivery_charge + luggage.discounted_price
        
        address = CustomerDetail.objects.filter(user=request.user)
        
        return render(request, 'core/buynow.html', {'final_price':final_price, 'luggage':luggage, 'address':address})
    else:
        return redirect("login")


def buynow_payment(request,id):

    if request.method == 'POST':
        selected_address_id = request.POST.get('buynow_selected_address')

    luggage = Luggage.objects.get(pk=id)     # cart_items will fetch product of current user, and show product available in the cart of the current user.
    delhivery_charge =200
    final_price= delhivery_charge + luggage.discounted_price
    # print("=============",final_price)
    address = CustomerDetail.objects.filter(user=request.user)
    #================= Paypal Code ======================================

    host = request.get_host()   # Will fecth the domain site is currently hosted on.

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': final_price,
        'item_name': 'Bags',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('buynowpaymentsuccess', args=[selected_address_id,id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    #========================================================================

    return render(request, 'core/payment.html', {'final_price':final_price,'address':address,'luggage':luggage,'paypal':paypal_payment})


def buynow_payment_success(request, selected_address_id, id):
    print('payment sucess',selected_address_id)
    
    user=request.user
    customer_data = CustomerDetail.objects.get(pk=selected_address_id)
    cart = Cart.objects.filter(user = request.user)
    luggage = Luggage.objects.get(pk=id)
    delivery_charge = 200
    final_price = delivery_charge + luggage.discounted_price
    
    luggage = Luggage.objects.get(pk=id)
    
    Order(user=user,customer=customer_data,product=luggage,quantity=1,total_price=final_price).save()
    
    return render(request, 'core/buynow_payment_success.html')


# ==============

    # rnyp zxor lgne zvzy  

def forgot_password(request):          
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(f'/reset_password/{uidb64}/{token}/')           
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_url}',
                'bharat2808singh@gmail.com',  # Use a verified email address
                [email],
                fail_silently=False,
            )
            return redirect('passresetinfo')
        else:
            messages.success(request,'please enter valid email address')
    return render(request, 'core/forgot_password.html')    


def reset_password(request, uidb64, token):
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return redirect('passwordresetdone')
                else:
                    return HttpResponse('Token is invalid', status=400)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return HttpResponse('Invalid link', status=400)
        else:
            return HttpResponse('Passwords do not match', status=400)
    return render(request, 'core/reset_password.html')

def password_reset_done(request):
    return render(request, 'core/password_reset_done.html')


def resetpassinfo(request):
    return render(request, 'core/reset_pass_info.html')