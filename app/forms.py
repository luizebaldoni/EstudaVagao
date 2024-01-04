from django import forms
from django.forms import ModelForm
from .models import *

# FORMULARIO DE REGISTRO

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

