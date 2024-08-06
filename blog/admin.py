# blog/admin.py

from django.contrib import admin
from .models import DividendPosts, Discussion

@admin.register(DividendPosts)
class DividendPostsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'writer', 'status', 'published_date')
    prepopulated_fields = {'slug': ('headline',)}
    search_fields = ['headline', 'body']
    list_filter = ['status', 'published_date']
    date_hierarchy = 'published_date'
    ordering = ['status', 'published_date']

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('article', 'commentator', 'approved', 'comment_date')
    search_fields = ['comment_text', 'commentator']
    list_filter = ['approved', 'comment_date']
    date_hierarchy = 'comment_date'
    ordering = ['approved', 'comment_date']

















