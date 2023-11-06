'''
ARQUIVO PARA DEFINIR OS TEMPLATES DA APLICAÇAO E OQ FAZEMOS COM ELES

'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration
from .models import Users



def Login(request_iter):
    return render(request_iter, 'registration/login.html')

def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == "POST": # Se o usuário prencheu o formulário:
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            login(request, Users)
            messages.success(request, ('Registrado com sucesso'))
            return redirect('register.html')
    else:
        form = UserRegistration()
        
    return render(request, 'register.html', {'form':form})
