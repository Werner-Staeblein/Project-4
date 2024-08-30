from django.db import models

# Create your models here.
# Guidance for this model was obtained from 
# https://pythonguides.com/contact-form-with-django-and-sqlite/
# but tuple/variable names customized. Field names likewise customized and
# changed


# Define tuples/variable names different from referenced learning material

CONTACT_MODE_CHOICES = (
    ("email", "E-Mail"),
    ("phone", "Phone"),
)

# Define tuples/variable names different from referenced learning material

QUESTION_CATEGORY_CHOICES = (
    ("dividends", "Dividends"),
    ("investment_strategies", "Investment Strategies"),
    ("stock_analysis", "Stock Analysis"),
    ("portfolio_management", "Portfolio Management"),
    ("taxation", "Taxation"),
    ("market_news", "Market News"),
    ("blog_content", "Blog Content"),
    ("technical_support", "Technical Support"),
    ("other", "Others"),
)

# Define classname camel-case distinctly different from reference material
# Use of different field names to extent that code remains readable/understandable

class UserContact(models.Model):
    """Model to store user contact information and inquiries."""
    
    name = models.CharField("Name", max_length=250)
    email = models.EmailField("Email")
    phone = models.CharField("Phone", max_length=15)
    
    mode_of_contact = models.CharField(
        "Contact by",
        max_length=10,
        choices=CONTACT_MODE_CHOICES,
        default='email'
    )
    
    question_type = models.CharField(
        "How can we help you?",
        max_length=50,
        choices=QUESTION_CATEGORY_CHOICES,
        default='dividends'
    )
    
    contactmessage = models.TextField("Message", max_length=3000)

    def __str__(self):
        return f"{self.name} - {self.email}"