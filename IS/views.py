from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, LoginForm


# Create your views here.
def front_page_loader(request):
    return render(request, "pages/front_page.html")
def catalogo_page(request):
    return render(request, "pages/catalogo.html")
def sobre_page(request):
    return render(request, 'pages/sobre.html')

def home_page(request):
    return render(request, 'pages/base_page_function.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Use the custom LoginForm
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('IS:front_page')  # Change 'home' to your desired landing page name
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()  # Initialize the form for GET request
    return render(request, 'pages/login_page.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('IS:login')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register_page.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('IS:front_page')
