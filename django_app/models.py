from django.db import models

'''
ARQUIVO PARA DEFINIR O BANCO DE DADOS, PARA AS ALTERAÇÕES AQUI FEITAS SEREM 
CARREGADAS DEVE-SE USAR O PROMPT DE COMANDO PARA EFETUAR AS ALTERAÇÕES
1º) py manage.py makemigrations
....
2º) py manage.py migrate
....
APOS ESTES DOIS COMANDOS O BANCO DE DADOS TERA SIDO ATUALIZADO
'''

class Users(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    numero = models.CharField(max_length=200, blank=True, null=True)
    senha = models.CharField(max_length=200, blank=True, null=True)
    estagio = models.CharField(max_length=200, blank=True, null=True)
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
