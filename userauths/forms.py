from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter full name",'class':"fullname"}))
    class Meta:
        model = User 
        fields = ['full_name', 'username', 'email','phone', 'password1', 'password2']  
