"""
NAO ALTERAR NADA NESTE ARQUIVO! PERMANECER COMO ESTA
ROTAS DEVEM SER ALTERADAS NO ARQUIVO URLS.PY NO DIRETORIO DJANGO_APP
"""
from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path("login/", views.index, name="login"),
	path('login/register/', views.register_user, name='register'),
]