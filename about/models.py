from django.db import models

class AboutPage(models.Model):
    heading = models.CharField(max_length=255)
    about_image = models.ImageField(upload_to='about_images/')
    last_update = models.DateTimeField(auto_now=True)
    about_text = models.TextField()

    def __str__(self):
        return self.heading