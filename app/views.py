'''
ARQUIVO PARA DEFINIR OS TEMPLATES DA APLICAÇAO E OQ FAZEMOS COM ELES
'''

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')