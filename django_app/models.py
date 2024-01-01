'''ARQUIVO PARA DEFINIR O LAYOUT DO BANCO DE DADOS'''
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, nome, email, password=None, **extra_fields):
        user = self.model(nome=nome, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, password=None, **extra_fields):
        user = self.create_user(nome, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    nome = models.CharField('username', max_length=200)
    numero = models.IntegerField('Número CMSM')
    estagio = models.IntegerField('Ano escolar')
    password = models.CharField('Senha', max_length=200)
    email = models.EmailField('Email', max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = ['numero', 'estagio', 'password', 'email']

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.nome

class Questions(models.Model):
    id_question = models.BigAutoField(primary_key = True)
    autor = models.TextField(max_length=200)
    data_envio = models.DateTimeField("data do envio")
    #verificado = models.ForeignKey(Users, on_delete = models.CASCADE)
    acessos = models.IntegerField(default=0)
    tag = models.TextField(max_length=200)
    pergunta = models.CharField(max_length=500)
    disciplina = models.TextField(max_length=500, default='DEFAULT VALUE')
    ano = models.IntegerField(default=0)
    nivel = models.TextField(max_length=500, default=0)

class respostas(models.Model):
    id_resp = models.BigAutoField(primary_key=True)
    autor = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='autor_resposta')
    data_envio = models.DateTimeField("data do envio")
    # verificado = models.ForeignKey(Users, on_delete = models.CASCADE)
    acessos = models.IntegerField(default=0)
    tag = models.TextField(max_length=200)
    resposta = models.TextField(max_length=500)
    aprovada = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='autor_aprovacao')