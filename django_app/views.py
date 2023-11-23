'''
ARQUIVO PARA DEFINIR OS TEMPLATES DA APLICAÇAO E OQ FAZEMOS COM ELES
'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration
from .models import Users
from django.conf import settings
from . import forms

# DEFINIÇÃO VIEW INICIAL (tela de login ou registro)
def Login(request):
    if not request.user.is_authenticated:
        return render(request, template_name='registration/login.html')
    return render(request, 'home.html')

# DEFINIÇÃO VIEW HOME (apos fzr login ou register)
def home(request):
    return render(request, 'home.html')

# DEFINIÇÃO VIEW DE LOGIN -- AINDA NÃO ESTÁ REDIRECIONANDO
def user_login(request):
    form = forms.UserRegistration()
    message = ''
    if request.method == 'POST':
        form = forms.UserRegistration(request.GET)
        if form.is_valid():
            username = form.cleaned_data['nome']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                message = "O login falhou!"
    return render(request, 'registration/login.html', context={'form': form, 'message': message})

# DEFINIÇÃO VIEW DE REGISTRO DO USUÁRIO -- AINDA NÃO ESTÁ REDIRECIONANDO
def cadastro(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})