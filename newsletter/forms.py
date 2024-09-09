from django import forms
from .models import NewsLetterSubscriber


class NewsLetterSubscriberForm(forms.ModelForm):

    """
    Form to subscribe to newsletter. Base is 'NewsLetterSubscriber' model.

    Form has fields for:
        - email: user email
        - name: user name

    """
    class Meta:
        model = NewsLetterSubscriber
        fields = ['email', 'name']
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter email'}
            ),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter name'}
            ),
        }
