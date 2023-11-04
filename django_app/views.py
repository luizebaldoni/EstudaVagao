from django import forms
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Users


def login(request_iter):
    return render(request_iter, 'registration/login.html')

def cadastro(request):
    novo_usuario = Users()
    novo_usuario.nome = request.POST.get('name')
    novo_usuario.numero = request.POST.get('numero')
    novo_usuario.estagio = request.POST.get('estagio')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.perfil_photo = request.POST.get('perfil_photo')
    novo_usuario.save()
    return render(request, 'register.html')