from django.shortcuts import render
from .models import AboutPage

# Create your views here.

def about_page(request):
    about_instance = AboutPage.objects.first()
    return render(request, 'about/about_page.html', {'about_instance': about_instance})
