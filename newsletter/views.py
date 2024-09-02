from django.shortcuts import render, redirect
from .forms import NewsLetterSubscriberForm
from django.contrib import messages

# Create your views here.


def subscription(request):
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
