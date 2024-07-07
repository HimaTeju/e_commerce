from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            "class": "w-1/2 py-4 px-4 rounded-xl", 
            "placeholder": "Enter Username"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "class": "w-1/2 py-4 px-4 rounded-xl", 
            "placeholder": "Enter Password"
    }))

class AddRetailerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
            "class": "w-1/2 py-4 px-4 rounded-xl", 
            "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
            "class": "w-1/2 py-4 px-4 rounded-xl", 
            "placeholder": "Enter Email Address"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            "class": "w-1/2 py-4 px-4 rounded-xl", 
            "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            "class": "w-1/2 py-4 px-4 rounded-xl", 
            "placeholder": "Confirm Password"
    }))