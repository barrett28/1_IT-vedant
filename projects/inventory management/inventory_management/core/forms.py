from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']