from django import forms
from django.forms import ModelForm
from .models import *

# FORMULARIO DE REGISTRO
class UserRegistration(ModelForm):
    class Meta:
        model = User #envia para a tabela Users do banco de dados
        fields = ['username', 'numero', 'password', 'email', 'estagio'] # colunas do banco
        widgets = {
            # definições de cada coluna
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'class': 'input'}), # precisa ser text pois é uma sequencia de numeros
            'estagio': forms.NumberInput(attrs={'placeholder': 'Ano escolar', 'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Senha'}),
            'username': forms.TextInput(attrs={'placeholder': 'Digite seu username', 'class': 'input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email', 'class': 'input'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

