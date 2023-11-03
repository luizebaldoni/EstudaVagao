from django.db import models

'''DEFININDO O LAYOUT DO BANCO DE DADOS'''

class Users(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    estagio = models.CharField(max_length=200)
    perfil_photo = models.ImageField(max_length=500)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['numero', 'estagio']

class Questions(models.Model):
    id_question = models.BigAutoField(primary_key = True)
    autor = models.ForeignKey(Users, on_delete = models.CASCADE)
    data_envio = models.DateTimeField("data do envio")
    #verificado = models.ForeignKey(Users, on_delete = models.CASCADE)
    acessos = models.IntegerField(default=0)
    tag = models.TextField(max_length=200)
    pergunta = models.TextField(max_length=500)
