from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserContactForm


def contact_view(request):

    """
    Handles the contact form submission and rendering.

    View processes the contact form when submitted via POST.
    If the form is valid, data is saved and displays a success message.
    With success, redirect of user.
    If the form is invalid, error message is shown.
    Error leads to form being rendered again with provided data.

    GET requests result in empty form rendered for user to populate.
    """

    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message was submitted successfully.'
            )
            return redirect('landing')
        else:
            messages.error(
                request,
                'An error occurred. Please check the form and try again.'
            )
    else:
        form = UserContactForm()

    return render(request, 'contact/contact.html', {'form': form})
