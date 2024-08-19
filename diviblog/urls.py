from django.contrib import admin
from django.urls import path, include
from diviblog import views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('', blog_views.landing, name='landing'),
    path('blog/', include('blog.urls')),
    path('test-404/', blog_views.test_404_view),
]

handler404 = 'diviblog.views.custom_404'


