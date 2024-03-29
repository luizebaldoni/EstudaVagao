from django import forms
from app.models import Author

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("fullname", "profile_pic")