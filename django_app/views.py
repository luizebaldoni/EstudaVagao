from django import forms
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Users


def index(request_iter):
    return render(request_iter, 'index.html')


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class RegisterForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'views_input',
            'style': 'padding: 15px; width: 100%; border-radius: 10px;',
            'placeholder': 'Username',
        }))
    numero = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'views_input',
            'style': 'padding: 15px; width: 100%; border-radius: 10px;',
            'placeholder': 'Numero',
        }))
    senha = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'views_input',
            'style': 'padding: 15px; width: 100%; border-radius: 10px;',
            'placeholder': 'Senha',
        }))
    estagio = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'views_input',
            'style': 'padding: 15px; width: 100%; border-radius: 10px;',
            'placeholder': 'Numero',
        }))
    perfil_photo =forms.ImageField()
    class Meta:
        model = Users
        fields = ('name',  'numero', 'senha', 'estagio', 'perfil_photo' )

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        User = form.save()
        if User:
            login(self.request, User)
        return super(RegisterView, self).form_valid(form)
