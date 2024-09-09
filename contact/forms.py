from django import forms
from .models import UserContact


class UserContactForm(forms.ModelForm):

    """
    Form to submit user contact information.

    Form based on UserContact model. Form collects user details.

    Attributes:
        Meta: Class that contains metadata for the form. Fields
        to be shown in the form.

    """
    class Meta:
        model = UserContact
        fields = ['name', 'email', 'phone', 'mode_of_contact',
                  'question_type', 'contactmessage']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'mode_of_contact': 'Contact by',
            'question_type': 'How can we help you?',
            'contactmessage': 'Message',
        }
