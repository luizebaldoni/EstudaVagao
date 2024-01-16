from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as lt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Author
from register.forms import UpdateForm


#usernames = [user.username for user in User.objects.all()]

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("home")
    context.update({
        "form":form, 
        "title": "Signup",
    })
    return render(request, "register/signup.html", context)

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    context.update({
        "form": form,
        "title": "Signin",
    })
    return render(request, "register/signin.html", context)

@login_required
def update_profile(request):
    user = request.user

    try:
        author = Author.objects.get(user=user)
    except Author.DoesNotExist:
        author = None

    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            updated_author = form.save(commit=False)

            # Verificar se o autor já tem um número associado e está tentando alterá-lo
            if author and author.fullname != updated_author.fullname:
                messages.error(request, 'Você já tem um número associado. Não é permitido alterar o número.')
                return redirect("update")

            # Verificar se o número fornecido já está associado a algum usuário
            existing_author = Author.objects.exclude(user=user).filter(fullname=updated_author.fullname).first()
            if existing_author:
                messages.error(request, f'O número {updated_author.fullname} já está associado ao usuário {existing_author.user.username}. Escolha outro número.')
                return redirect("update")

            # Salvar o autor apenas se a validação for bem-sucedida
            updated_author.save()
            messages.success(request, 'Perfil alterado com sucesso.')
            return redirect("home")
    return render(request, "register/update.html")

@login_required
def logout(request):
    lt(request)
    return redirect("signin")