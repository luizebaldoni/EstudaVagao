"""
 Arquivo para armazenar as rotas que serão utilizadas no projeto.
 Este arquivo armazenará as rotas do projeto em geral, é recomendável que cada aplicação
 do projeto possua um arquivo de rotas específico
"""
from django.urls import path, include
from django_app import views   

urlpatterns = [
    path("login/", views.index, name="login"),
	path('login/register/', views.register_user, name='register'),
]