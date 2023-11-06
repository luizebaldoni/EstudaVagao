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


'''
REDIRECIONAMENTO BÁSICO
'''

def Login(request):
    if not request.user.is_authenticated:
        return render(request, template_name='registration/login.html')
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')


'''
LOGIN -- AINDA NÃO ESTÁ REDIRECIONANDO
'''

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

'''
REGISTRO DO USUÁRIO -- AINDA NÃO ESTÁ REDIRECIONANDO
'''

def register_user(request):
    if request.method == 'POST':
        form = UserRegistration()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'GET':
        form = UserRegistration(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Você se registrou com sucesso.')
            login(request, form)
            return render(request, 'registration/login.html')
        else:
            return render(request, 'register.html', {'form': form})