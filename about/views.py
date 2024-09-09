from django.shortcuts import render
from .models import AboutPage

# For this view, I used
# https://docs.djangoproject.com/en/dev/ref/models/querysets/#first
# to understand that it is sufficient to simply retrieve the entire instance

# The instance retrieved is passed on as context variable to the template


def about_page(request):
    """
    Render about page. Information results from AboutPage model.

    View retrieves first instance of the AboutPage model and passes it to
    the template for rendering.

    """

    about_instance = AboutPage.objects.first()
    context = {
        'about_instance': about_instance
    }
    return render(request, 'about/about_page.html', context)
