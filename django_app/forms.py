'''ARQUIVO QUE DEFINE OS FORMULARIOS PRESENTES NO SERVIDOR E OS ENVIA PARA O BANCO'''

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *

# FORMULARIO DE REGISTRO
class UserRegistration(ModelForm):
    class Meta:
        model = Users #envia para a tabela Users do banco de dados
        fields = ['nome', 'numero', 'password', 'email', 'estagio'] # colunas do banco
        widgets = {
            # definições de cada coluna
            'numero': forms.TextInput(attrs={'placeholder': 'Número', 'class': 'input'}), # precisa ser text pois é uma sequencia de numeros
            'estagio': forms.NumberInput(attrs={'placeholder': 'Ano escolar', 'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Senha'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu username', 'class': 'input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email', 'class': 'input'}),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['nome', 'password']
    
    nome = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'nome'})
    )
    password = forms.CharField(
        label="Senha",
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'})
    )

'''
class LoginForm(AuthenticationForm):
    nome = forms.CharField( label="Username",max_length=30, widget=forms.TextInput(attrs=
        {'class': 'input', 'name': 'username', 'placeholder': 'Username' }
    ))
    password = forms.CharField( label="Senha",max_length=30,widget=forms.PasswordInput(attrs=
        {'class': 'input', 'Senha': 'password', 'placeholder': 'Senha'}
    ))
'''

class perguntaForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['pergunta', 'autor', 'ano', 'nivel', 'data_envio', 'disciplina']
        widgets = {
            # definições de cada coluna

            'pergunta': forms.Textarea(attrs={'placeholder': 'Faça sua pergunta', 'class': 'pergunta', 'cols': '100', 'rows': '4'}),
            'autor': forms.Textarea(attrs={'placeholder': 'Qual seu Numero? ', 'class': 'autor', 'cols': '15', 'rows': '1'}),
            'ano': forms.NumberInput(attrs={'placeholder': 'Qual seu ano?', 'class': 'ano'}),
            'nivel': forms.Select(choices=[(1, 'Facil'), (2, 'Médio'), (3, 'Difícil')], attrs={'class':'nivel'}),
            'data_envio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'data'}),
            'disciplina': forms.Select(choices=[(1, 'Portugues'), (2, 'Matematica'), (3, 'Quimica'), (4, 'Geografica'), (5, 'Historia'), (6, 'Fisica'), (7, 'Biologia'), (8, 'Ingles')], attrs={'class': 'disciplina'}),

        }