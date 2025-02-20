from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(label='First Name', label_suffix=' - ', initial='Naam Dalo')
    email = forms.EmailField(help_text='enter your email', widget=forms.TextInput(attrs={'placeholder':'enter you email'}))
    age = forms.IntegerField(min_value=15, max_value=25)
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget=forms.Textarea)