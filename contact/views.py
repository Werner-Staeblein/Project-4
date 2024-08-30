from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserContactForm

# Create your views here.


def contact_view(request):

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
