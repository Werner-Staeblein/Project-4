from .models import Discussion # My model is named "Discussion" and sites in the same folder, therefore the dot before models
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Discussion  
        fields = ('comment_text',)  
