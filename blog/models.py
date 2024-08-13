from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = ((0, "Draft"), (1, "Published"))

class DividendPosts(models.Model):									
    headline = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)	
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    body = models.TextField()	
    published_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)					
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)    							
									
    class Meta:			
        ordering = ["-published_date"]
	
    def __str__(self):
        return f"Article: {self.headline}"
									

class Discussion(models.Model):
    article = models.ForeignKey(DividendPosts, related_name="discussions", on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_discussions")
    comment_text = models.TextField()				
    approved = models.BooleanField(default=False)
    comment_date = models.DateTimeField(auto_now_add=True)
										
    class Meta:
        ordering = ["comment_date"]
		
    def __str__(self):
        return f"Comment by {self.commentator} on {self.article}"
