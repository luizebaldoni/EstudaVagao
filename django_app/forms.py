from django import forms
from django.forms import ModelForm
from .models import Users

class UserRegistration(ModelForm):
    class Meta:
        model = Users
        fields = ['nome', 'numero', 'password', 'email', 'estagio']
        widgets = {
        'numero': forms.NumberInput(attrs={'placeholder': 'Número'}),
        'estagio': forms.NumberInput(attrs={'placeholder': 'Número'}),
        'password': forms.PasswordInput(attrs={
            'class': 'input-text with-border', 'placeholder': 'Senha'}),
        'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome completo'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
        }