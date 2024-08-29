from django.shortcuts import render
from .models import AboutPage

# Create your views here.

## For this view, I used https://docs.djangoproject.com/en/dev/ref/models/querysets/#first
## to understand that it is sufficient to simply retrieve the entire instance

## The instance retrieved is passed on as context variable to the template


def about_page(request):
    about_instance = AboutPage.objects.first()
    return render(request, 'about/about_page.html', {'about_instance': about_instance})

