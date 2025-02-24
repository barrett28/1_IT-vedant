from django import forms
from django.core import validators

def start_width(val):
    x= val[0]
    if x.isdigit():
        raise forms.ValidationError("starting digit is not allowed")

class MarvelForms(forms.Form):
    name = forms.CharField(validators=[start_width])
    heroic_name = forms.CharField(validators=[validators.MaxLengthValidator(5)])