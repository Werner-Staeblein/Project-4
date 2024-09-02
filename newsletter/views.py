from django.shortcuts import render
from .forms import NewsLetterSubscriberForm

# Create your views here.

def subscription(request):
    if request.method == 'POST':
        form = NewsLetterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'newsletter/success.html')
    else:
        form = NewsLetterSubscriberForm()
    
    return render(request, 'newsletter/subscribe.html', {'form': form})
