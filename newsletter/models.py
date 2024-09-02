from django.db import models

# Create your models here.


class NewsLetterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} <{self.email}>"
