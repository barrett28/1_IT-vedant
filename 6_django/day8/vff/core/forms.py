from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confrim_pass = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        
        val_name = cleaned_data['name']
        val_password = cleaned_data['password']
        val_confrimpass = cleaned_data['confrim_pass']
        
        if len(val_name)<5:
            raise forms.ValidationError('please enter name greater than 5 character')
        
        if val_password!=val_confrimpass:
            raise forms.ValidationError('password does not match')