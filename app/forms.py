from django import forms
from django.forms import ModelForm
from .models import *
from django import forms 
from tinymce.widgets import TinyMCE 
from ckeditor.widgets import CKEditorWidget


class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False

class PostForm(forms.ModelForm):
    #content = forms.CharField(widget=CKEditorWidget())
    #content = HTMLField()
    content = forms.CharField(
        widget=TinyMCEWidget( 
            attrs={'required': False, 'cols': 10, 'rows': 5}), 
            label = "Sua pergunta", 
    )
    
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "ano_escolar", "tags"]
