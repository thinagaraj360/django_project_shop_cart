from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Customerform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter the username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'enter your password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'comfirm your password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']


