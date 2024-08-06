"""
URL configuration for testproject project.

"""
from django.contrib import admin
from django.urls import path
from blog import views as index_views

urlpatterns = [
    path('blog/', index_views.index, name="index"),
    path('admin/', admin.site.urls),
]


