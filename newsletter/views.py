from django.shortcuts import render, redirect
from .forms import NewsLetterSubscriberForm
from django.contrib import messages

# Create your views here.


def subscription(request):

    """
    Handles subscription form submission for newsletter.

    View processes newsletter subscription form when POST request exists.

    Valid form saves subscriber information and displays of success
    message to the user. Success leads to redirect to landing page.

    Invalid form leads to error message and form rendered again.

    GET request renders empty subscription form for user.

    """
    if request.method == 'POST':
        form = NewsLetterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for subscribing to our newsletter!'
            )
            return redirect('landing')
        else:
            messages.error(
                request,
                'An error occurred. Please check the form and try again.'
            )
    else:
        form = NewsLetterSubscriberForm()

    return render(request, 'newsletter/subscribe.html', {'form': form})
