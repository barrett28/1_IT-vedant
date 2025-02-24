from django import forms

class MarvelForms(forms.Form):
    name = forms.CharField()
    heroic_name = forms.CharField()