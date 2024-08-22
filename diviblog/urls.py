from django.contrib import admin
from django.urls import path, include
from blog.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('', landing, name='landing'),
    path('blog/', include('blog.urls')),
]

handler404 = 'diviblog.views.custom_404'
