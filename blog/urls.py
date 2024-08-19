from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<slug:post_slug>/', views.single_post, name='single_post'),
]
