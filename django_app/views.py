from django.shortcuts import render
from django.http import HttpResponse

def index(request_iter):
    return  render(request_iter,'index.html')

def cadastro(request_iter):
    return render(request_iter, 'cadastro.html')

