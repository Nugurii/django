from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=39, min_length=5)
    password = forms.CharField(max_length=128, min_length=8)

class SigninForm(forms.Form):
    username = forms.CharField(max_length=39, required=False)
    password = forms.CharField(max_length=128, required=False)

class DateForm(forms.Form):
    date = forms.CharField(widget=forms.TextInput(attrs={'class': 'home-form-control', 'autofocus': 'true', 'spellcheck': 'false'}), required=False)