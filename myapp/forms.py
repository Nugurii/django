from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=39, widget=forms.TextInput(attrs={'class': 'signup-form-control', 'autofocus': 'true', 'spellcheck': 'false'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'signup-form-control', 'autofocus': 'true'}))

class UserForm(forms.Form):
    username = forms.CharField(max_length=39, widget=forms.TextInput(attrs={'class': 'login-form-control', 'autofocus': 'true', 'spellcheck': 'false', 'id': 'username'}), required=False)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'login-form-control', 'autofocus': 'true', 'id': 'password'}), required=False)

class DateForm(forms.Form):
    date = forms.CharField(widget=forms.TextInput(attrs={'class': 'home-form-control', 'autofocus': 'true', 'spellcheck': 'false'}), required=False)