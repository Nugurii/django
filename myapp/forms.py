from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=39, widget=forms.TextInput(attrs={'class': 'form-control signup-form-control', 'autofocus': 'true', 'spellcheck': 'false', 'tabindex': '1', 'id': 'username'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control signup-form-control', 'autofocus': 'true', 'tabindex': '2', 'id': 'password'}))

class SigninForm(forms.Form):
    username = forms.CharField(max_length=39, widget=forms.TextInput(attrs={'class': 'form-control signin-form-control', 'autofocus': 'autofocus', 'spellcheck': 'false', 'tabindex': '1', 'id': 'username'}), required=False)
    password = forms.CharField(max_length=128,  widget=forms.PasswordInput(attrs={'class': 'form-control signin-form-control', 'autofocus': 'autofocus', 'tabindex': '2', 'id': 'password'}), required=False)

class DateForm(forms.Form):
    date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control home-form-control', 'autofocus': 'true', 'spellcheck': 'false', 'id': 'date'}), required=False)