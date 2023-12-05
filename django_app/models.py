'''ARQUIVO PARA DEFINIR O LAYOUT DO BANCO DE DADOS'''
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Users(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    nome = models.CharField('username', max_length=200)
    numero = models.IntegerField('Número CMSM')
    estagio = models.IntegerField('Ano escolar')
    password = models.CharField('Senha', max_length=200)
    email = models.EmailField('Email', max_length=200)
    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = ['numero', 'estagio', 'password', 'email']

class Questions(models.Model):
    id_question = models.BigAutoField(primary_key = True)
    autor = models.ForeignKey(Users, on_delete = models.CASCADE)
    data_envio = models.DateTimeField("data do envio")
    #verificado = models.ForeignKey(Users, on_delete = models.CASCADE)
    acessos = models.IntegerField(default=0)
    tag = models.TextField(max_length=200)
    pergunta = models.TextField(max_length=500)

class disciplinas(models.Model):
    id_disci = models.BigAutoField(primary_key=True)
    nivel = models.IntegerField(default=0)
    ano =  models.IntegerField(default=0)
    nome = models.TextField(max_length=500)

class respostas(models.Model):
    id_resp = models.BigAutoField(primary_key=True)
    autor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='autor_resposta')
    data_envio = models.DateTimeField("data do envio")
    # verificado = models.ForeignKey(Users, on_delete = models.CASCADE)
    acessos = models.IntegerField(default=0)
    tag = models.TextField(max_length=200)
    resposta = models.TextField(max_length=500)
    aprovada = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='autor_aprovacao')