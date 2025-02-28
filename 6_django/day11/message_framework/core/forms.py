from django import forms
from .models import MarvelModel

class MarvelForm(forms.ModelForm):
    class Meta:
        model = MarvelModel
        fields = ['name', 'heroic_name']
        
