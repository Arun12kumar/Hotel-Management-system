from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter full name",'class':"fullname"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter username",'class':"username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter email",'class':"email"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter phone number",'class':"phone"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter password",'class':"password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter confirm password",'class':"password"}))
    class Meta:
        model = User 
        fields = ['full_name', 'username', 'email','phone', 'password1', 'password2']  
