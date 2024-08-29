from django.db import models

from django.db import models

class AboutPage(models.Model):
    heading = models.CharField(max_length=255)
    about_image = models.ImageField(upload_to='about_images/')
    last_update = models.DateTimeField(auto_now=True)
    about_text = models.TextField()      
    intro = models.TextField(blank=True)
    my_story = models.TextField(blank=True)
    why_created = models.TextField(blank=True)
    comprehensive_analysis = models.TextField(blank=True)
    personalized_insights = models.TextField(blank=True)
    expert_opinions = models.TextField(blank=True)
    conclusion = models.TextField(blank=True)

    def __str__(self):
        return self.heading
    

    