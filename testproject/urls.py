"""
URL configuration for testproject project.

"""
from django.contrib import admin
from django.urls import path
from hello_world import views as index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', index_views.index, name="index"),
]
