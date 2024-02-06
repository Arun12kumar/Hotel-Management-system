from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from userauths.models import User,Profile
from userauths.forms import UserRegisterForm


# Create your views here.

def RegisterView(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        full_name = form.cleaned_data.get("full_name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(email=email, password=password)
        login(user)

        messages.success(request, f"Hey {full_name}, your account has been created sucessfully")
        
    context = {
        "form": form
    }
    return render(request,"userauths/sign-up.html", context)
