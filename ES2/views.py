
from django.http import HttpResponse
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, LoginForm





    

Exercicios = ["Caminhar 2.5km", "Jogar vôlei às 5hrs", "Tomar sol por 45min"]
# Create your views here.
def index(request): 
    return render(request, "html1/index.html")

def Exercicio(request):
    return render(request, "html1/Exercicio.html", {
        "Exercicios": Exercicios
    })



def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('ES2:login')
    else:
        form = UserRegisterForm()
    return render(request, 'html1/register_page.html', {'form': form})

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
                return redirect('ES2:home')  # Change 'home' to your desired landing page name
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()  # Initialize the form for GET request
    return render(request, 'html1/login_page.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('ES2:login')


def Invitation_view(request):
    return render(request, 'html1/Invitation_page.html')