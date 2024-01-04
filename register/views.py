from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as lt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from register.forms import UpdateForm


#usernames = [user.username for user in User.objects.all()]

def signup(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = AuthenticationForm()
    return render(request, 'register/signup.html', {'form': form})

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
    context = {}
    user = request.user
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("home")

    context.update({
        "form": form,
        "title": "Update Profile",
    })
    return render(request, "register/update.html", context)

@login_required
def logout(request):
    lt(request)
    return redirect("signin")