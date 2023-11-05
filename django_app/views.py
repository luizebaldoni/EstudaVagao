from django .shortcuts import render 
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration

def index(request_iter):
    return render(request_iter, "index.html")

def register_user(request):
    if request.method == "POST": # Se o usuário prencheu o formulário:
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            message.success(request, ("Registrado com sucesso"))
            return redirect("register.html")
    else:
        form = UserRegistration()
        
    return render(request, 'register.html', {"form":form})
