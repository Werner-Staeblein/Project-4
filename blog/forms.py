# My model is named "Discussion" and sits in the same folder.
# #Therefore the dot before models
from .models import Discussion
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ('comment_text',)
