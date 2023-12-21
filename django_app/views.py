'''
ARQUIVO PARA DEFINIR OS TEMPLATES DA APLICAÇAO E OQ FAZEMOS COM ELES

'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import TemplateView

from .forms import *
from .models import Users
from django.conf import settings
from . import forms


# DEFINIÇÃO VIEW DE LOGIN
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                form.add_error(None, "Nome de usuário ou senha incorretos")
        return render(request, 'home.html', {'form': form})

# DEFINIÇÃO VIEW DE REGISTRO DO USUÁRIO E JA REDIRECIONANDO
def cadastro(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})
# VIEW DE REALIZAR PERGUNTA
def pergunta(request):
    if request.method == 'POST':
        usuario= get_user_model()
        user_atual = request.user
        id = user_atual.id
        form = perguntaForm(request.POST, id)
        if form.is_valid():
            form.save()
            return render(request, 'pergunta.html')
    else:
        form = perguntaForm()
    return render(request, 'pergunta.html', {'form': form})