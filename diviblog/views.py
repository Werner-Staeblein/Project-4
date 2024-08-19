from django.shortcuts import render
from django.http import HttpResponse

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def test_404_view(request):
    return HttpResponse("Test 404 View")

