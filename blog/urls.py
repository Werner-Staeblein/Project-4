from django.urls import path
from .views import blog_index, blogpost_detail

urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('post/<slug:slug>/', blogpost_detail, name='single_post'),
]

