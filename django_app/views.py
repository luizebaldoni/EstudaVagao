from django.shortcuts import render

def index(request_iter):
    return  render(request_iter,'index.html')

def cadastro(request_iter):
    return render(request_iter, 'cadastro.html')