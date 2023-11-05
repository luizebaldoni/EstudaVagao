from django .shortcuts import render 
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration

def index(request_iter):
    return render(request_iter, "index.html")

class Login(View):
    def get(self,request):
        c = {}
        c.update(csrf(request))
        return render_to_response("index.html", c)
    def post(self,request):
        numero = request.get('Número CMSM','')
        password = request.get('Senha','')
        user = auth.authenticate(username = username, password = password)
        if(user is not None):
            auth.login(request,user)
            return True
        else:
            return False

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
