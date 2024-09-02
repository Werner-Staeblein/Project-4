from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscription, name='subscribe'),
]
