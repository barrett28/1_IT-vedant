from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from  .models import CustomerDetail


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
        }
        
        
class UserProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','date_joined','last_login']
        widgets= {'username':forms.TextInput(attrs={'placeholder': 'Enter username'}),
                  'first_name':forms.TextInput(attrs={'placeholder': 'Enter firstname'}),
                  'last_name':forms.TextInput(attrs={'placeholder': 'Enter lastname'}),
                  'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
                  'date_joined': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
                  'last_login': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                  }

class AdminProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields = '__all__'
        widgets= {'username':forms.TextInput(attrs={'placeholder': 'Enter username'}),
                  'email':forms.TextInput(attrs={'placeholder': 'Enter email'}),
                  'first_name':forms.TextInput(attrs={'placeholder': 'Enter firstname'}),
                  'last_name':forms.TextInput(attrs={'placeholder': 'Enter lastname'}),
                  }
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Old Passsword'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Confirm Password'}))


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = ['name', 'address', 'city', 'state', 'pincode']
        labels = {'name':'Full name'}
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'address':forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'city':forms.TextInput(attrs={'placeholder': 'Enter City Name'}),
            'state':forms.Select(attrs={'placeholder': 'Select State'}),
            'pincode':forms.NumberInput(attrs={'placeholder': 'Enter pincode'}),
        }


        

        