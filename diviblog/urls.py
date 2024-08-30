from django.contrib import admin
from django.urls import path, include
from blog.views import landing
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('', landing, name='landing'),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('contact/',include('contact.urls')),
]

handler404 = 'diviblog.views.custom_404'