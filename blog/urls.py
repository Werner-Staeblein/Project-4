from django.urls import path
from .views import blog_index, blogpost_detail, comment_edit, delete_comment

urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('post/<slug:slug>/', blogpost_detail, name='blogpost_detail'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>/',
         comment_edit, name='comment_edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/',
         delete_comment, name='delete_comment'),

]