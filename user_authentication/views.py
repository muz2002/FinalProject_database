from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can also associate the user with an account here
            login(request, user)
            return redirect("login")  # Redirect to the home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(dir(user))
            if user is not None:
                login(request, user)
                return redirect("account_detail")  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
