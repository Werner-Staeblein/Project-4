from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.landing, name='landing'),  # Landing page is in the root, the blog views.py manages the view
    path('blog/', include('blog.urls')),  # Include the blog app's URL configuration
]


