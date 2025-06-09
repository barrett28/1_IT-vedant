from .models import UserModel
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["user_name", "phone_number"]