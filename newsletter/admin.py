from django.contrib import admin
from .models import NewsLetterSubscriber

# Register your models here.

@admin.register(NewsLetterSubscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

