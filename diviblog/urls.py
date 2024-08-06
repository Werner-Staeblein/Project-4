"""
URL configuration for testproject project.

"""
from django.contrib import admin
from django.urls import path, include
from blog import views as index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('blog/', index_views.index, name="index"),
]


